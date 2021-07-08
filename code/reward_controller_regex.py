import sys

sys.path.append('regex-to-dfa')

from dfa import DFA
from dfa.draw import write_dot
from DFA import DFA as DFA2
import RegexToDFA

def old_to_new(D):
    N = list(D.Q)
    F = D.F
    
    def accepting(n):
        test = n in F
        for q in n:
            test = test | (q in F)
        return test
         
    D2 = DFA(
        start = N.index(D.q_0),
        inputs = D.Σ,
        label = lambda n: accepting(frozenset(N[n])), 
        transition = lambda n,a: N.index(D.δ(N[n],a)),
    )
    return D2

def regex_to_dfa(regex):
    D1 = RegexToDFA.obtain_dfa_from_regex(regex)
    return old_to_new(D1)

def R(machines,rewards,n):
    reward = 0
    for i in range(len(machines)):
        if machines[i]._label(n[i]): #if accepting, add the reward
            reward+=rewards[i]
    return reward

def location(i):
    return "dot/m" + str(i+1) + ".dot"

def combined_reward_controller(info):
    sequences = list(info.keys())
    rewards = list(info.values())
    machines = []
    for seq in sequences:
        new_dfa = regex_to_dfa(seq)
        machines.append(new_dfa)
        write_dot(new_dfa, location(sequences.index(seq)))
    if len(machines) == 0:
        return "error"
    product_automaton = machines[0]
    for i in range(1,len(machines)):
        product_automaton = product_automaton | machines[i]
    reward_controller = DFA(
    start = product_automaton.start,
    inputs = product_automaton.inputs,
    label = lambda n: R(machines,rewards,n) ,
    transition = product_automaton._transition,
    outputs = set.union({0},rewards),
    )
    return reward_controller

info = {"(b*ab*a)*b*" : 10, "a*ba*(ba*ba*)*" :15}

#D = regex_to_dfa("a*ba*(ba*ba*)*")
D = combined_reward_controller(info)

write_dot(D,"dot/RC1.dot")