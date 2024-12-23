from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 23

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

conns = [i.split("-") for i in data.splitlines()]
print(conns)

computers = [*[i[0] for i in conns], *[i[1] for i in conns]]
print(computers)

threes = set()

for c1, c2 in conns:
    c1c = set()
    c2c = set()
    for conn in conns:
        if c1 in conn:
            c1c |= set(conn)
        if c2 in conn:
            c2c |= set(conn)
    for third in c1c & c2c:
        if c1 == third or c2 == third:
            continue
        if c1.startswith("t") or c2.startswith("t") or third.startswith("t"):
            threes.add(frozenset({c1, c2, third}))

print(threes)
answer = len(threes)

print(answer)
# nie 39793
# pyperclip.copy(str(answer))