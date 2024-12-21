from collections import defaultdict

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 16

answer = 0
data = ''''''
data = load_test_data(DAY)
# data = load_data(DAY)


print_formatted(f"&e3&#ec{data}")

data = [[*i] for i in data.splitlines()]
print(data)

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

current = {start}

while current:
    print(points)
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
                points[((nx, ny), neigh)] = new_score
                new_current.add(((nx, ny), neigh))
    current = new_current.copy()

for ((x, y), rot), score in points.items():
    if (x, y) == end:
        answer = max(0, score)

print(answer)
# pyperclip.copy(str(answer))