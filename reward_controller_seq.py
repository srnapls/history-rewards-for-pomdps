from dfa import DFA 
from dfa.draw import write_dot

def reward_controller_from_sequences(sequences,omega):
    n_I = 0
    N = {n_I: {}}
    sigma = {}
    for seq in list(sequences.keys()):
        n = n_I
        for o in seq:
            if N[n].get(o) is None:
                n_new = len(N)
                N[n_new] = {}
                N[n][o] = n_new
            n = N[n][o]
        sigma[n] = sequences[seq]
    n_F = len(N)
    N[n_F] = {}
    for n in N:
        for o in omega:
            if N[n].get(o) is None:
                N[n][o] = n_F
        if sigma.get(n) is None:
            sigma[n] = 0
            
    return DFA(
        start = n_I,
        inputs = omega,
        label = lambda n: sigma[n], 
        transition = lambda n, o: N[n][o],
        outputs = set(sigma.values()),
     )