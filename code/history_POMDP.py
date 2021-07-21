from POMDP import POMDP 
from MDP import MDP
from dfa import DFA, dfa2dict
from reward_controller_regex import combined_reward_controller
from reward_controller_seq import create_reward_controller

class history_POMDP(POMDP):
    def __init__(self, prism, R,regex,T):
        self.T = T
        self.original_POMDP = POMDP(self, prism=prism)
        Omega = {str(o) for o in self.original_POMDP.Omega}
        if regex:
            self.N = combined_reward_controller(R,Omega)
        else:
            self.N = create_reward_controller(R,Omega)
        self.product_prism = self.build_product_pomdp()
 
 #todo: product_prism -->> product_pomdp of induced_pomdp
    def build_product_pomdp(self):
        (M, Omega, orig_O, _) = self.original_POMDP
        Omega = {str(o) for o in Omega}
        (orig_S, orig_s_0, A, orig_T) = M
        S = {(a,b) for a in orig_S for b in self.N.states()}
        s_0 = (orig_s_0, self.N._transition(self.N.start, str(orig_O[orig_s_0])))
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
        return POMDP(M = MDP(S, s_0, A, T), Omega = Omega, O = O, R = R)
        
    def create_prism_file(self):
        f = open("prism/reward_controlled_pomdp.prism", "w")
        content = ""
        content += "pomdp\n\n"
        content += "observables\n"
        content += "\to\n"
        content += "endobservables\n\n"
        content += "const int T = " + str(self.T) +";\n\n"
        content += "module model\n"
        
        def variable_declaration(var, start, end, init):
            return "\t" + var + " : [" + str(start) + " .. " + str(end) + "]\t init " + str(init) + ";\n"
            
        def internal_state_declaration(s, prob, s_new,final):
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
                string += "(o' = " + str(len(self.product_prism.Omega)) + ") & "
            elif self.product_prism.O[s] is not self.product_prism.O[s_new]:
                string += "(o' = " + str(self.product_prism.O[s_new]) + ") & "
            string += "(t' = t + 1) + "
            return string 
        
        s_0 = self.product_prism.M.s_0
        (s0, n0) = s_0
        o0 = self.product_prism.O[s_0]
        
        content += variable_declaration('t', 1, 'T', 1)
        content += variable_declaration('n', 0, len(self.N.states()) - 1, n0)
        content += variable_declaration('s', 0, len(self.original_POMDP.M.S) - 1, s0)
        content += variable_declaration('o', 0, len(self.product_prism.Omega), o0)
        content += "\n\n"
        
        def action_declaration(s, action,final):
            (s_, n_)  = s
            string   = "\t[" + action + "] (o = " + str(self.product_prism.O[s]) + ") & "
            string += "(s = " + str(s_) + ") & " 
            string += "(n = " + str(n_) + ") & "
            string += ("(t = T-1) -> " if final else "(t < T-1) -> ")
            return string
        
        for a in self.product_prism.M.A:
            for s1 in self.product_prism.M.S: 
                line1 = ""
                line2 = ""
                if self.product_prism.M.T[s1].get(a) is None:
                    continue
                line1 += action_declaration(s1, a, False)
                line2 += action_declaration(s1, a, True)
                for s2 in self.product_prism.M.S:
                    line1+= internal_state_declaration(s1, self.product_prism.M.T[s1][a].get(s2), s2, False)
                    line2 += internal_state_declaration(s1, self.product_prism.M.T[s1][a].get(s2), s2, True)
                line1 = line1[:-3]
                line2 = line2[:-3]
                content += line1 + ";\n" + line2 + ";\n"
            content += "\n"
        
        content += "\t[end] (o != " + str(len(self.product_prism.Omega)) +") -> 1:(o' = "+ str(len(self.product_prism.Omega)) + ");\n\n"
        
        content += "endmodule\n\n"
        content += "label \"end\" = o=2;\n\n"
        
        content += "rewards \"profit\"\n"
        visited_nodes = []
        for s in self.product_prism.M.S:
            (s_, n_) = s
            if  n_ in visited_nodes:
                continue 
            r = self.product_prism.R[s]
            visited_nodes.append(n_)
            if r == 0:
                continue 
            content += "\t[end]\t (n = " + str(n_) + "): " + str(r) + ";\n" 
        for a in self.product_prism.M.A:
            content += "\t[" + a + "]\t true:\t 0;\n"
        content += "endrewards"

        f.write(content)
        f.close()
        
        f = open("prism/properties.pctl", "w")
        f.write("R{\"profit\"}max=? [F \"end\"]")
        f.close()

if __name__ == '__main__':
    R = {"aa":15,"bab":20,"aaba":12,"b":2}
    R2 = {"(b*ab*a)*b*" : 10, "a*ba*(ba*ba*)*" :15}
    R3 = {"(1*01*0)*1*" :10, "0*10*(10*10*)*" :15}
    R4= {"(1*01*0)*1*" :10}
    model = history_POMDP("prism/simple_pomdp.prism", R3, True, 10)
    model.create_prism_file()