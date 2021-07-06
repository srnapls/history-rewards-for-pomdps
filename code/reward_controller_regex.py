import sys

sys.path.append('regex-to-dfa')

from dfa import DFA
from dfa.draw import write_dot
from DFA import DFA as DFA2
import RegexToDFA

rewards_regex = [10,15]

def T1(s,a):
    if a=='b':
        return s
    if s==0:
        return 1
    else :
        return 0

dfa_even_a =  DFA(
    start = 0,
    inputs={'a','b'},
    label = lambda s: s==0,
    transition = T1,
    )
    
def T2(s,a):
    if a=='a':
        return s
    if s==0:
        return 1
    else :
        return 0


dfa_odd_b = DFA(
    start = 0,
    inputs={'a','b'},
    label = lambda s: s==1,
    transition = T2,
   )

machines = [dfa_even_a, dfa_odd_b]

write_dot(dfa_even_a, "dot/dfa3.dot")
write_dot(dfa_odd_b,"dot/dfa4.dot")

combined = dfa_even_a | dfa_odd_b

def R(s):
    reward = 0
    for i in range(len(machines)):
        if machines[i]._label(s[i]): #if accepting, add the reward
            reward+=rewards_regex[i]
    return reward

reward_controller = DFA(
    start = combined.start,
    inputs = combined.inputs,
    label = R, 
    transition = combined._transition,
    outputs = set.union({0},rewards_regex),
    )

def old_to_new(D):
    N = list(D.Q)
    delta = D.δ_dict
    
    D2 = DFA(
    start = 0,
    inputs = D.Σ,
    label = lambda n: N[n] in D.F, 
    transition = lambda n,a: N.index(D.δ(N[n],a)),
   )
    return D2

def regex_to_dfa(regex):
    return old_to_new(RegexToDFA.obtain_dfa_from_regex(regex))

D2= regex_to_dfa("aa")

write_dot(reward_controller,"dot/rc.dot")
write_dot(D2,"dot/aa.dot")
