import stormpy
import stormpy.core
                        
class POMDP:
    def __init__(self, M=None, Omega=None, O=None,prism=None):
        if prism == None:
            self.M = MDP
            self.Omega = Omega
            self.O = O 
            self.R = R
        else:
            program = stormpy.parse_prism_program(prism)
            model = stormpy.build_model(program)
            states = model.states
            S= []
            A = set()
            for s in states:
                S.append(s.id)
                A.add(s.actions.id)
            s_0 = model.initial_states[0]
            T = {}
            for s in 
            

