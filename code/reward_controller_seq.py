from dfa import DFA 
from dfa.draw import write_dot

omega = ['a','b']

def CreateRewardController(seq,rew):
    assert len(seq) == len(rew)
    N = {0:[None,None]}
    sigma = [None]
    for i in range(len(seq)):
        n = list(N.keys())[0]
        for o in seq[i]:
            if N[n][omega.index(o)] is None:
                n_new = len(N)
                N[n_new] = [None,None]
                N[n][omega.index(o)] = n_new
                sigma.append(None)
            n = N[n][omega.index(o)]
        sigma[n] = rew[i]
    n_F = len(N)
    N[n_F] = [None,None]
    sigma.append(None)
    for n in N:
        for o in omega:
            if N[n][omega.index(o)] is None:
                N[n][omega.index(o)] = n_F
        if sigma[n] is None:
            sigma[n] = 0
    nodes = list(N.keys())
    n_I = nodes[0]
    delta = list(N.values())
    
    reward_controller = DFA(
        start = n_I,
        inputs = omega,
        label = lambda n: sigma[n], 
        transition = lambda n, a: delta[n][omega.index(a)],
        outputs = set(sigma),
     )
    return reward_controller


sequences = ["aa","bab","aaba","b"]
r = [15,20,12,2] 

rc = CreateRewardController(sequences,r)
write_dot(rc,"dot/rc2.dot")