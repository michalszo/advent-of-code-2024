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

# DIAGONALS >v
for x in range(len(data[0]) - 2):
    for y in range(len(data) - 2):
        s1 = "".join(data[y+i][x+i] for i in range(3))
        s2 = "".join(data[y+(2-i)][x+i] for i in range(3))
        if s1 in ["MAS", "SAM"] and s2 in ["MAS", "SAM"]:
            answer += 1

# 1905
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))