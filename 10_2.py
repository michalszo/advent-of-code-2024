from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 10

answer = 0
# data = '''89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732'''
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = data.splitlines()
width, height = len(data[0]), len(data)
data = {x + 1j * y: int(v) for x, row in enumerate(data) for y, v in enumerate(row)}
print(data)

zeros = {k for k, v in data.items() if v == 0}
print(zeros)

for start in zeros:
    paths = {tuple([start])}

    for number in range(9):
        new_paths = set()
        for path in paths:
            point = path[-1]
            for direction in {-1j, 1, 1j, -1}:
                new_pos = point + direction
                if new_pos not in data.keys():
                    continue
                if data[new_pos] == number + 1:
                    new_paths.add(path + tuple([new_pos]))
        paths = new_paths.copy()
    answer += len(paths)
    print(paths)

# 1511
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))