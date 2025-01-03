from string_formatting import print_formatted
from util import *
import itertools as it
from collections import defaultdict
import math

DAY = 18

answer = 0
data = ''''''
# data = load_test_data(DAY); size = 7
data = load_data(DAY); size = 71
print_formatted(f"&e3&#ec{data}")

data = [tuple(int(j) for j in i.split(",")) for i in data.splitlines()]

points = {data.pop(0)}

#SKIP

while (new_point := data.pop(0)) != (64, 68):
    points.add(new_point)

for entries in range(1000000000):
    if not data:
        break
    new_point = data.pop(0)
    points.add(new_point)
    print(new_point)

    current = {(0, 0)}
    costs = defaultdict(lambda: math.inf)
    costs[(0, 0)] = 0

    while current:
        new_current = set()
        # print(current)
        for x, y in current:
            cost = costs[(x, y)]
            new_cost = cost + 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < size and 0 <= ny < size):
                    continue
                if (nx, ny) in points:
                    continue
                if costs[(nx, ny)] <= new_cost:
                    continue
                costs[(nx, ny)] = new_cost
                new_current.add((nx, ny))
        current = new_current.copy()

    # for y in range(size):
    #     for x in range(size):
    #         if (x, y) in points:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print()
    # for y in range(size):
    #     for x in range(size):
    #         if (x, y) in costs.keys():
    #             print("O", end="")
    #         elif (x, y) in points:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    #
    # print(costs[(size-1, size-1)])

    # print(costs)
    if math.isinf(costs[(size-1, size-1)]):
        # print(entries)
        answer = new_point
        break

answer = f"{answer[0]},{answer[1]}"

# 56,8
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))