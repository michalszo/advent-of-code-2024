from string_formatting import print_formatted
from util import *
import itertools as it
from collections import defaultdict

DAY = 6

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

rotations = [-1j, 1, 1j, -1]

data = [i for i in data.splitlines()]
the_map = defaultdict(int)

for y, row in enumerate(data):
    for x, v in enumerate(row):
        xy = x + 1j * y
        if v == "^":
            guard = xy
        the_map[xy] = 1 if v == "#" else -1

print(the_map)

start_pos = guard
possible_obstacles = {guard}
rot = 0

while 1:
    new_pos = guard + rotations[rot]
    if the_map[new_pos] == 1:
        rot = (rot + 1) % 4
    elif the_map[new_pos] == -1:
        guard = new_pos
        possible_obstacles.add(guard)
    elif the_map[new_pos] == 0:
        break


possible_obstacles.remove(start_pos)

print(possible_obstacles)

# working_obstacles = set()

for obstacle in possible_obstacles:
    print(obstacle)
    guard = start_pos
    rot = 0
    visited = {(guard, rot)}
    while 1:
        new_pos = guard + rotations[rot]
        if the_map[new_pos] == 1 or new_pos == obstacle:
            rot = (rot + 1) % 4
        elif the_map[new_pos] == -1:
            guard = new_pos
        elif the_map[new_pos] == 0:
            break
        if (guard, rot) in visited:
            # print((guard, rot), visited)
            # for y, row in enumerate(data):
            #     for x, v in enumerate(row):
            #         if (x + 1j * y) == obstacle:
            #             print("O", end="")
            #         elif (x + 1j * y) == guard:
            #             print("B", end="")
            #         elif (x + 1j * y) in {i[0] for i in visited} and v != "^":
            #             print("X", end="")
            #         else:
            #             print(v, end="")
            #     print()
            # print()
            answer += 1
            break
        visited.add((guard, rot))

# 1530
print(answer)
# pyperclip.copy(str(answer))