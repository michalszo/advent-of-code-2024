from string_formatting import print_formatted
from util import *
import itertools as it
from collections import defaultdict

DAY = 8

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [i for i in data.splitlines()]

width, height = len(data[0]), len(data)

frequencies = defaultdict(set)
for y, row in enumerate(data):
    for x, v in enumerate(row):
        if v != ".":
            frequencies[v].add(x + 1j * y)

print(frequencies)

antinodes = set()
for nodes in frequencies.values():
    for start, end in it.permutations(nodes, 2):
        new_antinode = end + (end - start)
        if 0 <= new_antinode.real < width and 0 <= new_antinode.imag < height:
            antinodes.add(new_antinode)

print(antinodes)
answer = len(antinodes)

# 336
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))