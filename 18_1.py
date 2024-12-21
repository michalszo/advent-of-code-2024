import math
from collections import defaultdict

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 18

answer = 0
data = ''''''
# data = load_test_data(DAY); entries = 12; size = 7
data = load_data(DAY); entries = 1024; size = 71

print_formatted(f"&e3&#ec{data}")

data = [tuple(int(j) for j in i.split(",")) for i in data.splitlines()][:entries]

for y in range(size):
    for x in range(size):
        if (x, y) in data:
            print("#", end="")
        else:
            print(".", end="")
    print()

print(data)

current = {(0, 0)}
costs = defaultdict(lambda: math.inf)
costs[(0, 0)] = 0

while current:
    new_current = set()
    print(current)
    for x, y in current:
        cost = costs[(x, y)]
        new_cost = cost + 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < size and 0 <= ny < size):
                continue
            if (nx, ny) in data:
                continue
            if costs[(nx, ny)] <= new_cost:
                continue
            costs[(nx, ny)] = new_cost
            new_current.add((nx, ny))
    current = new_current.copy()

# print(costs)
answer = costs[(size-1, size-1)]

print(answer)
# pyperclip.copy(str(answer))