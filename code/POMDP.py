import stormpy
import stormpy.core

from MDP import MDP

                        
class POMDP:

    counter = 0
    
    def __init__(self, M=None, Omega=None, O=None,prism=None):
        if prism == None:
            self.M = MDP
            self.Omega = Omega
            self.O = O
        else:
            program = stormpy.parse_prism_program(prism)
            model = stormpy.build_model(program)
            states = model.states
            S= []
            A = set()
            Omega = set()
            O = {}
            T = {}
            actions_per_observations = {}
            transitional_matrix = model.transition_matrix
            for s in states:
                state = s.id
                T[state] = {}
                S.append(s.id)
                observation = model.get_observation(s)
                O[state] = observation
                if observation in Omega:
                    actions = actions_per_observations[observation]
                else:
                    Omega.add(observation)
                    actions = []
                    for a in list(s.actions):
                        action_label = self.fresh_actions_name()
                        A.add(action_label)
                        actions.append(action_label)    
                    A.update(actions)
                    actions_per_observations[observation] = actions
                start = transitional_matrix.get_row_group_start(s)
                end = transitional_matrix.get_row_group_end(s)
                assert len(range(start,end)) == len(actions)
                for i in range(0,len(actions)):
                    T[state][actions[i]] = {}
                    for entry in transitional_matrix.get_row(i+start):
                        T[state][actions[i]][entry.column] = entry.value()
            s_0 = model.initial_states
            self.M = MDP(S,s_0,A,T)
            self.Omega = Omega
            self.O = O
            
    def fresh_actions_name(self):
        self.counter += 1
        return "action" + str(self.counter)
    
    def __str__(self):
        string = ""
        string += str(self.M)
        return string
            
if __name__ == '__main__':
    model = POMDP(prism="prism/simple_pomdp.prism")
    print(model)