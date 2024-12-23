from string_formatting import print_formatted
from util import *
from collections import Counter

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 2

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [[int(j) for j in i.split()] for i in data.splitlines()]
print(data)

for line in data:
    anyy = False
    for i in range(-1, len(line)):
        i_line = line.copy()
        if i != -1:
            del i_line[i]
        diff = {b-a for a, b in zip(i_line, i_line[1:])}
        if diff <= {1, 2, 3} or diff <= {-1, -2, -3}:
            answer += 1
            break

# 536
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))