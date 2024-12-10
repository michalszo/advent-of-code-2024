from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 10

answer = 0
data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = [[int(j) for j in i] for i in data.splitlines()]
width, height = len(data[0]), len(data)
print(data)

zeros = [(x, y) for x, y in it.product(range(width), range(height)) if data[y][x] == 0]
print(zeros)

for start in zeros:
    points = {start}

    for number in range(9):
        new_points = set()
        for x, y in points:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # if dx == dy == 0:
                #     continue
                if not (0 <= y + dy < height and 0 <= x + dx < width):
                    continue
                if data[y+dy][x+dx] == number + 1:
                    new_points.add((x+dx, y+dy))
        points = new_points.copy()
    answer += len(points)
    print(points)

print(answer)
# pyperclip.copy(str(answer))