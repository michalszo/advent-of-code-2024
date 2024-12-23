from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 4

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [i for i in data.splitlines()]
print(data)

# HORIZONTALS
for row in data:
    for x in range(len(row) - 3):
        s = row[x:x+4]
        if s in ["XMAS", "SAMX"]:
            answer += 1

# VERTICALS
for x in range(len(data[0])):
    for y in range(len(data) - 3):
        s = "".join(data[y+i][x] for i in range(4))
        if s in ["XMAS", "SAMX"]:
            answer += 1

# DIAGONALS >v
for x in range(len(data[0]) - 3):
    for y in range(len(data) - 3):
        s = "".join(data[y+i][x+i] for i in range(4))
        if s in ["XMAS", "SAMX"]:
            answer += 1

# DIAGONALS <^
for x in range(len(data[0]) - 3):
    for y in range(len(data) - 1, 2, -1):
        # print(y, len(data))
        s = "".join(data[y-i][x+i] for i in range(4))
        if s in ["XMAS", "SAMX"]:
            answer += 1

# 2613
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))