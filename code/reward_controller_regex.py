import sys

sys.path.append('regex-to-dfa')

from dfa import DFA,dfa2dict
from dfa.draw import write_dot
from DFA import DFA as DFA2
import RegexToDFA

counter = 0

def rename(D):
    N = list(D.states())
    return DFA(
        start = N.index(D.start),
        inputs = D.inputs,
        label = lambda n: D._label(N[n]), 
        transition = lambda n, a: N.index(D._transition(N[n], a)),
        outputs = D.outputs
    )

def regex_to_dfa(regex, omega):
    D = RegexToDFA.obtain_dfa_from_regex(regex,omega)
    N = list(D.Q)
    def accepting(n):
        test = n in D.F
        for q in n:
            test = test or (q in D.F)
        return test
         
    D2 = DFA(
        start = N.index(D.q_0),
        inputs = D.Σ,
        label = lambda n: accepting(frozenset(N[n])), 
        transition = lambda n,a: N.index(D.δ(N[n],a)),
    )
    return rename(D2)

def union(machines, rewards):
    assert len(machines)==len(rewards)
    
    if len(machines)==1:
        D = machines[0]
        return DFA(
            start = D.start,
            inputs = D.inputs,
            transition = D._transition,
            label = lambda s: rewards[0] if D._label(s) else 0,
            outputs = set.union({0},rewards),
        )
    return DFA(
        start=tuple([m.start for m in machines]),
        inputs = machines[0].inputs,
        transition = lambda s,c: tuple([machines[i]._transition(s[i],c) for i in range(len(machines))]),
        label = lambda s: sum([rewards[i] for i in range(len(machines)) if machines[i]._label(s[i])]),
        outputs = set.union({0},rewards),
    )

def fresh():
    global counter
    counter += 1
    return "dot/m" + str(counter) + ".dot"

def reward_controller_from_regex(info,omega):
    machines = [rename(regex_to_dfa(seq, omega)) for seq in list(info.keys())]
    for m in machines:
        write_dot(m, fresh())
    tmp = rename(union(machines, list(info.values())))
    write_dot(tmp, "dot/RC2_test.dot")
    return tmp
    
if __name__ == '__main__':
    R = {"aaba" :15}
    R2 = {"(b*ab*a)*b*" : 10, "a*ba*(ba*ba*)*" :15}
    R4 = {"a*bcc*" :12}
    omega = {'1','0'}
    R3 = {"(1*01*0)*1*" :10}
    
    write_dot(reward_controller_from_regex(R,{'a','b'}),"dot/RC_test.dot")