#import reward_controller_seq
#import reward_controller_regex


class MDP:
    def __init__(self, S, s_0, A, T):
        self.S = S
        self.s_0 = s_0
        self.A = A
        self.T = T
    
    def __str__(self): 
        print_statement = "Actions available: " + str(A)
        for s_I in S:
            for a in A:
                for s_N in S:
                    p = T(s_I, a, s_N)
                    if p!=0:
                        print_statement += "From " + s_I + " to " + s_N " + with action " + a + " has probability " + p