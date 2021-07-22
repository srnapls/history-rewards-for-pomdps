
from collections import defaultdict
from functools import reduce
import prettytable


class FA:
    def __init__(self, Q, Σ, δ_dict, q_0, F):
        self.Q = Q
        self.Σ = Σ
        self.δ_dict = δ_dict
        self.q_0 = q_0
        self.F = F
        self.extra = set()

    def δ(self, q, a):
        return self.δ_dict[q][a]

    def __str__(self):
        desc = prettytable.PrettyTable(['Parameter', 'Value'])
        desc.add_row(["Q", "{%s}" % ', '.join(str(q) for q in self.Q)])
        desc.add_row(["Σ", "{%s}" % ', '.join(self.Σ)])
        desc.add_row(["q_0", str(self.q_0)])
        desc.add_row(["F", "{%s}" % ', '.join(str(f) for f in self.F)])
        if self.extra:
            desc.add_row(["Extra Symbols", self.extra])
        delta = prettytable.PrettyTable(['δ'] + list(self.Σ.union(self.extra)))
        for q in self.Q:
            delta.add_row([q] + [self.δ(q, a) for a in self.Σ.union(self.extra)])
        desc.add_row(["δ", str(delta)])
        return str(desc)


class DFA(FA):
    def __init__(self, Q, Σ, δ_dict, q_0, F):
        '''assert set(δ_dict.keys()).intersection(Q) == Q
        assert all(
            set(δ_dict[d].keys()).intersection(Σ) == Σ
            and all(x in Q for x in δ_dict[d].values())
            for d in δ_dict)
        assert q_0 in Q
        assert F <= Q  # Subset or Equal'''
        FA.__init__(self, Q, Σ, δ_dict, q_0, F)

    def rename(self, start=0):
        rename_dict = dict(zip(self.Q, {'q%s' % (start + i) for i in range(len(self.Q))}))

        def rename_func(x):
            return rename_dict[x]

        Q = set(map(rename_func, self.Q))
        q_0 = rename_func(self.q_0)
        F = set(map(rename_func, self.F))
        new_delta = defaultdict(dict)
        for q, A in self.δ_dict.items():
            for a in A:
                new_delta[rename_func(q)][a] = rename_func(self.δ_dict[q][a])
        return DFA(Q, self.Σ, new_delta, q_0, F)

    def is_accepted(self, w):
        try:
            return reduce(self.δ, w, self.q_0) in self.F
        except KeyError:
            return False

    def draw(self, filename, prog='dot', format='png'):
        G = pgv.AGraph(directed=True, rankdir='LR')
        G.add_node('qi', shape='point')
        for q in self.Q:
            G.add_node(q, shape='oval', peripheries=2 if q in self.F else 1)
        G.add_edge('qi', self.q_0, label='start')
        for u in self.δ_dict:
            for a, v in self.δ_dict[u].items():
                label = G.get_edge(u, v).attr['label'] + ',' + a if G.has_edge(u, v) else a
                G.add_edge(u, v, label=label)
        G.draw(filename, format=format, prog=prog)

    def union(self, M):
        assert self.Σ == M.Σ
        Q = {(x, y) for x in self.Q for y in M.Q}
        delta_dict = {(x, y): {a: (self.δ(x, a), M.δ(y, a)) for a in self.Σ} for (x, y) in Q}
        F = {(x, y) for x in self.Q for y in M.Q if x in self.F or y in M.F}
        return DFA(Q, self.Σ, delta_dict, (self.q_0, M.q_0), F)

    def intersection(self, M):
        assert self.Σ == M.Σ
        Q = {(x, y) for x in self.Q for y in M.Q}
        delta_dict = {(x, y): {a: (self.δ(x, a), M.δ(y, a)) for a in self.Σ} for (x, y) in Q}
        F = {(x, y) for x in self.F for y in M.F}
        return DFA(Q, self.Σ, delta_dict, (self.q_0, M.q_0), F)

    def difference(self, M):
        assert self.Σ == M.Σ
        Q = {(x, y) for x in self.Q for y in M.Q}
        delta_dict = {(x, y): {a: (self.δ(x, a), M.δ(y, a)) for a in self.Σ} for (x, y) in Q}
        F = {(x, y) for x in self.F for y in M.F if x in self.F and y not in M.F}
        return DFA(Q, self.Σ, delta_dict, (self.q_0, M.q_0), F)

    def compliment(self):
        return DFA(self.Q, self.Σ, self.δ_dict, self.q_0, self.Q - self.F)

    def reduce(self):
        state_pairs = {frozenset({x, y}) for x in self.Q for y in self.Q if x != y}
        non_distinguishable_pairs = set()
        non_distinguishable_states = set()
        distinguishable_pairs = {x for x in state_pairs if len(set(x).intersection(self.F)) == 1}

        def is_distinguishable(pair):
            # Recursive Discovery of Distinguishable Pairs with Memory Function
            if len(pair) == 1:
                return False
            if pair in distinguishable_pairs:
                return True
            else:
                distinguishable = False
                for a in self.Σ:
                    next_pair = frozenset(map(lambda x: self.δ(x, a), pair))
                    distinguishable = distinguishable or (len(next_pair.difference(pair)) == 0)
                if distinguishable:
                    distinguishable_pairs.update({pair})
                    return True 
                for a in self.Σ:
                    next_pair = frozenset(map(lambda x: self.δ(x, a), pair))
                    if is_distinguishable(next_pair):
                        distinguishable_pairs.update({pair})
                        return True
                return False

        for pair in state_pairs:
            bb = is_distinguishable(pair)
            if not bb:
                non_distinguishable_pairs.update({pair})
                non_distinguishable_states.update(pair)

        def transitive_closure(array):
            if len(array) == 0:
                return set()
            new_list = [frozenset(array.pop(0))]  # initialize first set with value of index `0`

            for item in array:
                for i, s in enumerate(new_list):
                    if any(x in s for x in item):
                        new_list[i] = new_list[i].union(item)
                        break
                else:
                    new_list.append(frozenset(item))
            return set(new_list)

        non_distinguishable_pairs = transitive_closure(list(non_distinguishable_pairs))
        

        Q = non_distinguishable_pairs.union({frozenset(x) for x in set(self.Q) - non_distinguishable_states})
        delta_dict = defaultdict(dict)
        for q in Q:
            for a in self.Σ:
                if len(self.δ_dict[q]) == len(self.Σ):
                    intermediate = {x for x in Q if  self.δ(q, a) in x}
                    if len(intermediate) == 0:
                        delta_dict[q][a] = self.δ(q, a)
                    else:
                        delta_dict[q][a] = list(intermediate)[0]
                else:
                    S = set()
                    for q1 in q:
                        q2 = self.δ(q1, a)
                        if q2 not in q:
                            S.add(frozenset(q2))
                    S = frozenset(S)
                    if len(S) == 0:
                        delta_dict[q][a] = q
                    elif len(S) == 1:
                        S = list(S)[0]
                        if S in Q:
                            delta_dict[q][a] = S
                        else: 
                            delta_dict[q][a] = list({q_n for q_n in Q if S in q_n})[0]
                    else:
                        delta_dict[q][a] = list({q_n for q_n in Q if S.issubset(q_n)})[0]
        if self.q_0 in Q:
            q_0 = self.q_0
        else:
            q_0 = [x for x in Q if self.q_0 in x][0]
        D = DFA(Q, self.Σ, delta_dict, q_0, self.F)
        return D