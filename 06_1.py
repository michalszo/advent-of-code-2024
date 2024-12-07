from collections import defaultdict

import numpy as np

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 6

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = [i for i in data.splitlines()]

rotations = [(0, -1), (1, 0), (0, 1), (-1, 0)]

gx, gy = -1, -1
rot = 0

mapa = defaultdict(int)

def add_pos(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]

def sub_pos(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]

for y, row in enumerate(data):
    for x, v in enumerate(row):
        if v == "^":
            gx, gy = x, y
        if v == "#":
            mapa[(x, y)] = 1
        else:
            mapa[(x, y)] = -1

assert -1 not in (gx, gy)

visited = {(gx, gy)}

while 1:
    print(gx, gy, rot)
    nx, ny = add_pos((gx, gy), rotations[rot % 4])
    if mapa[(nx, ny)] == 1:
        rot += 1
        gx, gy = add_pos((gx, gy), rotations[rot % 4])
        visited.add((gx, gy))
        continue
    elif mapa[(nx, ny)] == -1:
        gx, gy = nx, ny
        visited.add((gx, gy))
        continue
    elif mapa[(nx, ny)] == 0:
        break

print(mapa)

answer = len(visited)

print(answer)
# pyperclip.copy(str(answer))