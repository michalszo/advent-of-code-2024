from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 7

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [i.split(": ") for i in data.splitlines()]
data = {int(i[0]): [int(j) for j in i[1].split()] for i in data}
print(data)

for result, numbers in data.items():
    values = {numbers[0]}
    for n in numbers[1:]:
        new_values = set()
        for v in values:
            new_values.add(v * n)
            new_values.add(v + n)
            new_values.add(int(str(v) + str(n)))
        values = new_values.copy()
    if result in values:
        answer += result

# 189207836795655
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))