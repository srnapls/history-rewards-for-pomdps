class MDP:
    def __init__(self, S, s_0, A, T):
        self.S = S
        self.s_0 = s_0
        self.A = A
        self.T = T
    
    def __iter__(self):
        return iter((self.S, self.s_0, self.A, self.T))
        
    def prob(self,s_I, a, s_N):
        info = self.T[s_I]
        if info.get(a) is None:
            return 0
        elif info[a].get(s_N) is None:
            return 0
        else:
            return info[a][s_N]
    
    def __str__(self): 
        print_statement = "Actions available: " + str(self.A) + "\n"
        for s_I in self.S:
            for a in self.A:
                for s_N in self.S:
                    p = self.prob(s_I, a, s_N)
                    if p!=0:
                        print_statement += "From %i to %i with %s has probability %f.\n" % (s_I, s_N, a, p)
        return print_statement