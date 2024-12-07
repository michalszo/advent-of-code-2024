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

og = (gx, gy)
og_rot = rot
visited = {(gx, gy)}

while 1:
    nx, ny = add_pos((gx, gy), rotations[rot])
    if mapa[(nx, ny)] == 1:
        rot = (rot + 1) % 4
        gx, gy = add_pos((gx, gy), rotations[rot])
        visited.add((gx, gy))
        continue
    elif mapa[(nx, ny)] == -1:
        gx, gy = nx, ny
        visited.add((gx, gy))
        continue
    elif mapa[(nx, ny)] == 0:
        break

visited.remove(og)

for obstacle in visited:
    # print(obstacle)
    gx, gy = og
    rot = og_rot

    super_visited = {(gx, gy, rot)}
    while 1:
        nx, ny = add_pos((gx, gy), rotations[rot])
        if mapa[(nx, ny)] == 1 or (nx, ny) == obstacle:
            rot = (rot + 1) % 4
            # gx, gy = add_pos((gx, gy), rotations[rot])
        elif mapa[(nx, ny)] == -1:
            gx, gy = nx, ny
        elif mapa[(nx, ny)] == 0:
            break
        if (gx, gy, rot) in super_visited:
            answer += 1
            break
        super_visited.add((gx, gy, rot))

print(answer)
# 1430 źle
# pyperclip.copy(str(answer))