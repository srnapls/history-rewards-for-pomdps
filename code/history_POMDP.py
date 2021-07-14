#import pomdp 

class history_POMDP(POMDP):
    def __init__(self, prism, R,T):
        self.T = T
        self.R = R
        POMDP.__init__(self, prism=prism)
        
    