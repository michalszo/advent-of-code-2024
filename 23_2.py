from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 23

answer = 0
# data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

conns = {frozenset(i.split("-")) for i in data.splitlines()}
print(conns)

# computers = [*[i[0] for i in conns], *[i[1] for i in conns]]
# print(computers)

longest = frozenset()

for conn1 in conns:
    cs = {i: set() for i in conn1}
    for conn2 in conns:
        for c, s in cs.items():
            if c in conn2:
                s |= set(conn2)
    ns = set.intersection(*cs.values()) - conn1
    pairs = {frozenset(i) for i in it.combinations(ns, 2)} & conns
    # print(conn1, ns, pairs)
    groups = [frozenset({i}) for i in ns]
    # print(groups)
    while groups:
        for group1 in groups:
            cs = {i: set() for i in group1}
            for new in ns:
                for c, s in cs.items():
                    if frozenset({c, new}) in pairs:
                        s.add(new)
        # print(cs)
        ns = set.intersection(*cs.values()) - group1
        # print(group1, ns)
        new_groups = [frozenset({*group1, i}) for i in ns]
        if not new_groups:
            break
        groups = new_groups.copy()
    # print("G", groups)
    for group in groups:
        big_group = group | conn1
        if len(big_group) > len(longest):
            longest = big_group

answer = ",".join(sorted(longest))

# hf,hz,lb,lm,ls,my,ps,qu,ra,uc,vi,xz,yv
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))