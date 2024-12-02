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
        diff = [b-a for a, b in zip(i_line, i_line[1:])]
        if False not in [i > 0 for i in diff] and False not in [1 <= abs(i) <= 3 for i in diff]:
            anyy = True
            continue
        if False not in [i < 0 for i in diff] and False not in [1 <= abs(i) <= 3 for i in diff]:
            anyy = True
            continue
    if anyy:
        answer += 1

print(answer)
# pyperclip.copy(str(answer))