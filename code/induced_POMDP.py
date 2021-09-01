from POMDP import POMDP 
from MDP import MDP
from dfa import DFA, dfa2dict

from reward_controller_regex import reward_controller_from_regex
from reward_controller_seq import reward_controller_from_sequences

class induced_POMDP(POMDP):
    def __init__(self, prism, R,regex,T):
        self.T = T
        self.original_POMDP = POMDP(self, prism=prism)
        Omega = {str(o) for o in self.original_POMDP.Omega}
        if regex:
            self.N = reward_controller_from_regex(R, Omega)
        else:
            self.N = reward_controller_from_sequences(R, Omega)
        self.product_pomdp = self.build_product_pomdp()
 
    def build_product_pomdp(self):
        (M, Omega, orig_O, _) = self.original_POMDP
        Omega = {str(o) for o in Omega}
        (orig_S, orig_s_0, A, orig_T) = M
        S = {(a,b) for a in orig_S for b in self.N.states()}
        s_0 = (orig_s_0, self.N._transition(self.N.start, str(orig_O[orig_s_0])))
        A.add("end")
        O = {}
        T = {}
        R = {}
        for s1 in S:
            T[s1] = {}
            (s_1, n_1) = s1
            O[s1] = orig_O[s_1]
            R[s1] = self.N._label(n_1)
            for a in A:
                if orig_T[s_1].get(a) is None:
                    continue
                T[s1][a] = {}
                for s2 in S:
                    (s_2, n_2) = s2
                    if orig_T[s_1][a].get(s_2) is None:
                        continue
                    if self.N._transition(n_1, str(O[s1])) is n_2 :
                        T[s1][a][s2] = orig_T[s_1][a][s_2]
        final_state = "s_F"
        S.add(final_state)
        O[final_state] = len(Omega)
        R[final_state] = 0
        T[final_state] = {}
        for s in S:
            T[s]["end"] = {}
            T[s]["end"][final_state] = 1
        return POMDP(M = MDP(S, s_0, A, T), Omega = Omega, O = O, R = R)
        
    def create_prism_file(self):
        f = open("prism/reward_controlled_pomdp.prism", "w")
        content   = "pomdp\n\n"
        content += "observables\n"
        content += "\to\n"
        content += "endobservables\n\n"
        content += "const int T = " + str(self.T) +";\n\n"
        content += "module model\n"
        
        def variable_declaration(var, start, end, init):
            return "\t" + var + " : [" + str(start) + " .. " + str(end) + "]\t init " + str(init) + ";\n"
            
        def internal_state_declaration(s, prob, s_new, final):
            (s1, n1) = s 
            (s2, n2) = s_new 
            string = ""
            if prob is None:
                return string
            string += str(prob) + ":" 
            if s1 is not s2:
                string += "(s' = " + str(s2) + ") & " 
            if n1 is not n2:
                string += "(n' = " + str(n2) + ") & "
            if final:
                string += "(o' = " + str(len(self.product_pomdp.Omega)) + ") & "
            elif self.product_pomdp.O[s] is not self.product_pomdp.O[s_new]:
                string += "(o' = " + str(self.product_pomdp.O[s_new]) + ") & "
            string += "(t' = t + 1) + "
            return string 
        
        s_0 = self.product_pomdp.M.s_0
        (s0, n0) = s_0
        content += variable_declaration('t', 1, 'T', 1)
        content += variable_declaration('n', 0, len(self.N.states()) - 1, n0)
        content += variable_declaration('s', 0, len(self.original_POMDP.M.S) - 1, s0)
        content += variable_declaration('o', 0, len(self.product_pomdp.Omega), self.product_pomdp.O[s_0])
        content += "\n\n"
        
        def action_declaration(s, action, final):
            (s_, n_)  = s
            string   = "\t[" + action + "] (o = " + str(self.product_pomdp.O[s]) + ") & "
            string += "(s = " + str(s_) + ") & " 
            string += "(n = " + str(n_) + ") & "
            string += ("(t = T-1) -> " if final else "(t < T-1) -> ")
            return string
        
        for a in self.product_pomdp.M.A:
            if a == "end":
                content += "\t[end] (o != " + str(len(self.product_pomdp.Omega)) + ") -> 1:(o' = " + str(len(self.product_pomdp.Omega)) + ");\n\n"
                continue
            for s1 in self.product_pomdp.M.S: 
                if s1 == "s_F":
                    continue
                line1 = ""
                line2 = ""
                if self.product_pomdp.M.T[s1].get(a) is None:
                    continue
                line1 += action_declaration(s1, a, False)
                line2 += action_declaration(s1, a, True)
                for s2 in self.product_pomdp.M.S:
                    if s2 == "s_F":
                        continue
                    line1+= internal_state_declaration(s1, self.product_pomdp.M.T[s1][a].get(s2), s2, False)
                    line2 += internal_state_declaration(s1, self.product_pomdp.M.T[s1][a].get(s2), s2, True)
                line1 = line1[:-3]
                line2 = line2[:-3]
                content += line1 + ";\n" + line2 + ";\n"
            content += "\n"
            
        content += "endmodule\n\n"
        content += "label \"end\" = o = "+ str(len(self.product_pomdp.Omega)) + ";\n\n"
        
        content += "rewards \"profit\"\n"
        
        for a in self.product_pomdp.M.A:
            visited_nodes = []
            if a == "end":
                for s in self.product_pomdp.M.S:
                    if s == "s_F":
                        continue
                    (s_, n_) = s
                    if  n_ in visited_nodes or self.product_pomdp.R[s] == 0:
                        continue 
                    visited_nodes.append(n_)
                    content += "\t[end]\t (n = " + str(n_) + "): " + str(self.product_pomdp.R[s]) + ";\n" 
            else:
                content += "\t[" + a + "]\t true:\t 0;\n"
        content += "endrewards"

        f.write(content)
        f.close()
        
        f = open("prism/properties.pctl", "w")
        f.write("R{\"profit\"}max=? [F \"end\"]")
        f.close()

if __name__ == '__main__':
    R = {"00":15,"101":20,"0010":12,"1":2}
    R2 = {"(b*ab*a)*b*" : 10, "a*ba*(ba*ba*)*" :15}
    R3 = {"(1*01*0)*1*" :10, "0*10*(10*10*)*" :15}
    R4= {"(1*01*0)*1*" :10}
    
    R_example = {"(0|1|3)*":100, "(0|1|3)*2(0|1|3)*":50, "(0|1|3)*2(0|1|3)*2(0|1|3)*":25, "(0|1|3)*2(0|1|3)*2(0|1|3)*2(0|1|3)*": 10}
    model = induced_POMDP("prism/obstacle.prism", R_example, True, 15)
    model.create_prism_file()