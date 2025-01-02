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

visited = {guard}
rot = 0

while 1:
    print(guard, rot)
    new_pos = guard + rotations[rot]
    if the_map[new_pos] == 1:
        rot = (rot + 1) % 4
        # We don't move here, because there can be an obstacle in the new direction too
        # guard += rotations[rot % 4]
        # visited.add(guard)
    elif the_map[new_pos] == -1:
        guard = new_pos
        visited.add(guard)
    elif the_map[new_pos] == 0:
        break


answer = len(visited)

# 4663
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))