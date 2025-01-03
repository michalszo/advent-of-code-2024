from collections import defaultdict

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 12

answer = 0
data = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [list(i) for i in data.splitlines()]
print(data)

letters = defaultdict(set)
for y, row in enumerate(data):
    for x, v in enumerate(row):
        letters[v].add((x, y))

print(letters)

for l, els in letters.items():
    while els:
        x, y = els.pop()
        ppp = {(x, y)}
        data[y][x] = f"{l}{x}{y}"
        while ppp:
            npp = set()
            for ix, iy in ppp:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = ix+dx, iy+dy
                    if (nx, ny) in els:
                        els.remove((nx, ny))
                        npp.add((nx, ny))
                        data[ny][nx] = f"{l}{x}{y}"
            ppp = npp.copy()

    # for x1, y1 in els:
    #     neighbors = 0
    #     for x2, y2 in els:
    #         if abs(x1-x2) == 1 or abs(y1-y2) == 1:
    #             neighbors += 1
    #     if not neighbors:
    #         data[y1][x1] = f"{l}{x1}{y1}"

print(data)


# width, height = len(data[0]), len(data)

points = defaultdict(lambda: defaultdict(int))
area = defaultdict(int)

for y, row in enumerate(data):
    for x, v in enumerate(row):
        area[v] += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            nx, ny = 2*x+dx+1, 2*y+dy+1
            points[v][(nx, ny)] += 1
            # if (nx, ny) in points[v]:
            #     points[v].remove((nx, ny))
            #     double_used[v].add((nx, ny))
            # elif (nx, ny) not in double_used[v]:
            #     points[v].add((nx, ny))
        # for dx, dy in []:
        #     nx, ny = 2*x+dx, 2*y+dy
            # if (nx, ny) in points[v]:
            #     points[v].remove((nx, ny))
            #     double_used[v].add((nx, ny))
            # elif (nx, ny) not in double_used[v]:
            # points[v].add((nx, ny))
        # points[v] |= {(x+dx, y+dy) }
        # print(x, y, v)

print(points)

edges = defaultdict(set)

for v, counts in points.items():
    for (x, y), c in counts.items():
        if (y % 2 != 0 or x % 2 != 0) and c > 1:
            continue
        if y % 2 == 0 and x % 2 == 0 and c > 3:
            continue
        edges[v].add((x, y))

for v, points in edges.items():
    sides = 0
    # print(v, points)
    for x, y in points.copy():
        if (x-1, y) in points and (x+1, y) in points and (x, y-1) in points and (x, y+1) in points:
            points.remove((x, y))
    while points:
        x, y = points.pop()
        # if x == 6 and y == 6:
        #     print((x-1, y) in points, (x+1, y) in points, (x, y-1) in points, (x, y+1) in points)
        # if (x-1, y) in points and (x+1, y) in points and (x, y-1) in points and (x, y+1) in points:
        #     print(x, y)
        #     continue
        # sides[v].add({(x, y)})
        current = x_side = {(x, y, -1), (x, y, 1)}
        while current:
            new_points = set()
            for ix, iy, dx in current:
                nx, ny = ix+dx, iy
                if (nx, ny) in points:
                    points.remove((nx, ny))
                    new_points.add((nx, ny, dx))
                elif (ix, iy) != (x, y):
                    points.add((ix, iy))
            current = new_points.copy()
            x_side |= new_points
        if len(x_side) > 2:
            sides += 1
            print(x_side)

        current = y_side = {(x, y, -1), (x, y, 1)}
        while current:
            new_points = set()
            # print("DD", current)
            for ix, iy, dy in current:
                nx, ny = ix, iy + dy
                # print("SS", nx, ny)
                if (nx, ny) in points:
                    points.remove((nx, ny))
                    new_points.add((nx, ny, dy))
                elif (ix, iy) != (x, y):
                    points.add((ix, iy))
            current = new_points.copy()
            y_side |= new_points
        if len(y_side) > 2:
            sides += 1
            # print(y_side)
    print(v, area[v], sides, area[v]*sides)
    answer += area[v]*sides

# 902742
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))