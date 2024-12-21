import math
from collections import defaultdict

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 20

answer = 0
data = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''
# data = load_test_data(DAY)
data = load_data(DAY)


print_formatted(f"&e3&#ec{data}")

data = [[*i] for i in data.splitlines()]
# print(data)

rots = (0 - 1j, 1 + 0j, 0 + 1j, -1 + 0j)

size = (len(data[0]), len(data))

mapa = defaultdict(bool)

for y, row in enumerate(data):
    for x, v in enumerate(row):
        pos = x + y*1j
        if data[y][x] == "#":
            mapa[pos] = False
        elif data[y][x] == ".":
            mapa[pos] = True
        elif v == "S":
            start = pos
            mapa[pos] = True
        elif v == "E":
            end = pos
            mapa[pos] = True

assert start is not None and end is not None

# print(data)
print(start, end)

def distances_to_point(_point):
    distances = {_point: 0}

    current = {_point}
    used = set()

    while current:
        # print(points)
        new_current = set()
        for point in current:
            score = distances[point]
            for difference in rots:
                new_point = point + difference
                if not (0 <= new_point.real < size[0] and 0 <= new_point.imag < size[1]):
                    continue
                # if new_point in current:
                #     continue
                new_score = score + 1
                if not mapa[new_point]:
                    continue
                if new_point not in distances.keys() or score <= distances[new_point]:
                    distances[new_point] = new_score
                    new_current.add(new_point)
        current = new_current.copy()
        used |= current

    return distances

distances_to_start = distances_to_point(start)
distances_to_end = distances_to_point(end)

total_time = distances_to_start[end]

cheated_times = defaultdict(int)

for x, y in it.product(range(size[0]), range(size[1])):
    cheat_point = x + 1j*y
    cheat_time = math.inf
    for dentry, dexit in it.permutations(rots, 2):
        entry_point = cheat_point+dentry
        exit_point = cheat_point+dexit
        # if (x, y) == (5, 7):
        #     print(entry_point, exit_point)
        if entry_point in distances_to_start.keys() and exit_point in distances_to_end.keys():
            a = distances_to_start[entry_point]
            b = distances_to_end[exit_point]
            cheat_time = min(cheat_time, a + b + 2)
            # if (x, y) == (5, 7):
            #     print(entry_point, exit_point, a, b)
    cheated_time = total_time - cheat_time
    if math.isinf(cheat_time):
        continue
    if cheated_time >= 100:
        answer += 1
    cheated_times[cheated_time] += 1

print(cheated_times)

# ps = math.inf
#
# for ((x, y), rot), score in points.items():
#     if (x, y) == end:
#         ps = min(ps, score)

print(answer)
# pyperclip.copy(str(answer))