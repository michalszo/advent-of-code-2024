from collections import defaultdict

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 8

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = [i for i in data.splitlines()]

width, height = len(data[0]), len(data)

def sub_pos(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]

def add_pos(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]

frequencies = defaultdict(set)
for y, row in enumerate(data):
    for x, v in enumerate(row):
        if v != ".":
            frequencies[v].add((x, y))

print(frequencies)

antinodes = set()
for nodes in frequencies.values():
    for start, end in it.permutations(nodes, 2):
        inc = sub_pos(end, start)
        new_antinode = add_pos(start, inc)
        while 1:
            if 0 <= new_antinode[0] < width and 0 <= new_antinode[1] < height:
                antinodes.add(new_antinode)
            else:
                break
            new_antinode = add_pos(new_antinode, inc)

print(antinodes)

for y in range(height):
    for x in range(width):
        if (x, y) in antinodes:
            print("#", end="")
        else:
            print(".", end="")
    print()

# for nodes in frequencies.values():
#     antinodes -= nodes

answer = len(antinodes)

print(answer)
# pyperclip.copy(str(answer))