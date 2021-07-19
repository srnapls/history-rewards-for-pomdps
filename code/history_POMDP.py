from POMDP import POMDP 
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
    
    def build_product_pomdp(self):
        (M, Omega, orig_O) = self.original_POMDP
        Omega = {str(o) for o in Omega}
        (orig_S, orig_s_0, A, orig_T) = M
        S = {(a,b) for a in orig_S for b in self.N.states()}
        s_0 = (orig_s_0, self.N._transition(self.N.start, str(orig_O[orig_s_0])))
        O = {}
        for (s,n) in S:
            O[(s,n)] = orig_O[s]
        T = {}
        for s1 in S:
            T[s1] = {}
            for a in A:
                (s_1, n_1) = s1
                if orig_T[s_1].get(a) is None:
                    continue
                T[s1][a] = {}
                for s2 in S:
                    (s_2, n_2) = s2
                    if orig_T[s_1][a].get(s_2) is None:
                        continue
                    if self.N._transition(n_1, str(O[s1])) is n_2 :
                        T[s1][a][s2] = orig_T[s_1][a][s_2]
        
    def create_prism_file(self):
        f = open("prism/reward_controlled_pomdp.prism", "w")
        content = ""
        content += "pomdp\n\n"
        content += "observables\n"
        content += "\t o\n"
        content += "endobservables\n\n"
        content += "const int T = " + str(self.T) +";\n\n"
        content += "module model:\n"
        f.write(content)
        f.close()
        
if __name__ == '__main__':
    R = {"aa":15,"bab":20,"aaba":12,"b":2}
    R2 = {"(b*ab*a)*b*" : 10, "a*ba*(ba*ba*)*" :15}
    R3 = {"(1*01*0)*1*" :10}
    model = history_POMDP("prism/simple_pomdp.prism", R3, True, 10)
    model.create_prism_file()