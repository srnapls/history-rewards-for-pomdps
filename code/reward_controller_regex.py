import sys

sys.path.append('regex-to-dfa')

from dfa import DFA,dfa2dict
from DFA import DFA as DFA2
import RegexToDFA

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
    

def union(machines,rewards):
    assert len(machines)==len(rewards)
    
    def T(s,c):
        transitions = []
        for i in range(len(machines)):
            transitions.append(machines[i]._transition(s[i],c))
        return tuple(transitions)
        
    def R(s):
        reward = 0
        for i in range(len(machines)):
            if machines[i]._label(s[i]):
                reward += rewards[i]
        return reward 
    
    if len(machines)==1:
        D = machines[0]
        r = rewards[0]
        return DFA(
            start = D.start,
            inputs = D.inputs,
            transition = D._transition,
            label = lambda s: r if D._label(s) else 0,
            outputs = set.union({0},rewards),
        )
    return DFA(
        start=tuple([m.start for m in machines]),
        inputs = machines[0].inputs,
        transition = T,
        label = lambda s: R(s),
        outputs = set.union({0},rewards),
    )

def combined_reward_controller(info,omega):
    sequences = list(info.keys())
    rewards = list(info.values())
    machines = []
    for seq in sequences:
        new_dfa = rename(regex_to_dfa(seq, omega))
        machines.append(new_dfa)
    reward_controller = rename(union(machines, rewards))
    #write_dot(reward_controller, "dot/RC_test.dot")
    return reward_controller
    
if __name__ == '__main__':
    R = {"aa":15,"bab":20,"aaba":12,"b":2}
    R2 = {"(b*ab*a)*b*" : 10, "a*ba*(ba*ba*)*" :15}
    R4 = {"a*bcc*" :12}
    omega = {'0','1'}
    R3 = {"(1*01*0)*1*" :10}
    combined_reward_controller(R3,omega)