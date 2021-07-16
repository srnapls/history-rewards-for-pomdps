from pomdp import pomdp 
from dfa import DFA

class history_POMDP(POMDP):
    def __init__(self, prism, R,regex,T):
        self.T = T
        self.R = R
        self.regex=regex
        self.original_POMDP = POMDP(self, prism=prism)
        self.product_prism = self.build_product_pomdp
        
    