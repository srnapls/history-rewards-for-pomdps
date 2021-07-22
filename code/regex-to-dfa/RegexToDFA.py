import subprocess
from antlr4 import *
from collections import defaultdict

if __name__ is not None and "." in __name__:
    from .RegExParser import RegExParser
    from .RegExLexer import RegExLexer
    from .RegExVisitor import RegExVisitor
    from .DFA import DFA
else:
    from RegExParser import RegExParser
    from RegExLexer import RegExLexer
    from RegExVisitor import RegExVisitor
    from DFA import DFA

def rename(Q, q_0, T, F, sigma):
    new_state = frozenset({0})
    Q = list(Q)
    for i in range(len(Q)):
        if len(Q[i])==0:
            temp = T[Q[i]]
            Q[i] = new_state
            T[Q[i]] = temp
        for a in sigma:
            if len(T[Q[i]][a]) == 0:
                T[Q[i]][a] = new_state
    if len(q_0)==0:
        q_0 = new_state
    for q in F:
        if len(q)==0:
            q= new_state
    return (Q, q_0, T, F)
    

def regex_to_dfa(root, visitor,sigma):
    Dstates = [frozenset(root.firstpos)]
    Dtran = defaultdict(dict)
    q_0 = frozenset(root.firstpos)
    queue = [frozenset(root.firstpos)]
    while queue:
        S = queue.pop(0)
        for a in sigma:
            U = set()
            if len(S) == 0:
                Dtran[S][a]=S
            for p in S:
                if visitor.charmap[p - 1] == a:
                    U = U.union(visitor.followpos[p])
                U = frozenset(U)
                if U not in Dstates:
                    Dstates.append(U)
                    queue.append(U)
                Dtran[S][a] = U
    F = {q for q in Dstates if len(visitor.charmap) in q}
    (Dstates, q_0, Dtran, F) = rename(Dstates, q_0, Dtran, F, sigma)
    return DFA(Q=Dstates, Σ=sigma, δ_dict=Dtran, q_0=q_0, F=F)
    
def obtain_dfa_from_regex(regex,sigma):
    with open('test.txt', "w") as file:
        file.writelines([regex, '\n'])
    input_file = FileStream('test.txt')
    lexer = RegExLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = RegExParser(stream)
    tree = parser.prog()
    visitor = RegExVisitor()
    root = visitor.visit(tree)
    D = regex_to_dfa(root,visitor,sigma)
    return D.reduce()
