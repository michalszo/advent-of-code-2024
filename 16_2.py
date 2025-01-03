from string_formatting import print_formatted
from util import *
import itertools as it
from collections import defaultdict

DAY = 16

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [[*i] for i in data.splitlines()]

rots = ((0, -1), (1, 0), (0, 1), (-1, 0))

for y, row in enumerate(data):
    for x, v in enumerate(row):
        if v == "S":
            start = ((x, y), 1)
            data[y][x] = "."
        if v == "E":
            end = (x, y)
            data[y][x] = "."

assert start is not None and end is not None

print(data)
print(start, end)

points = {start: 0}
paths = defaultdict(set)
paths[(start[0], 0)] = {start}

current = {start}

while current:
    # print(points)
    new_current = set()
    for point in current:
        (x, y), rot = point
        score = points[point]
        for neigh in [(rot-1)%4, rot, (rot+1)%4]:
            nx, ny = x+rots[neigh][0], y+rots[neigh][1]
            if data[ny][nx] == "#":
                continue
            new_score = score + 1
            if neigh != rot:
                new_score += 1000
            if ((nx,ny), neigh) not in points.keys() or score <= points[((nx, ny), neigh)]:
                paths[((nx, ny), new_score)] |= paths[((x, y), score)] | {(nx, ny)}
                points[((nx, ny), neigh)] = new_score
                new_current.add(((nx, ny), neigh))
    current = new_current.copy()


for ((x, y), rot), score in points.items():
    if (x, y) == end:
        best_score = max(0, score)

tiles = paths[(end, best_score)]

print(tiles)
answer = len(tiles)

# 494
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))