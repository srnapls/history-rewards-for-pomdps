from dfa import DFA 
from dfa.draw import write_dot

omega = ['a','b']

def CreateRewardController(sequences):
    seq = list(sequences.keys())
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
        sigma[n] = sequences[seq[i]]
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


sequences = {"aa":15,"bab":20,"aaba":12,"b":2}

rc = CreateRewardController(sequences)
write_dot(rc,"dot/rc2.dot")