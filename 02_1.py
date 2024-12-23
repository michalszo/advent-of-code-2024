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
    diff = {b-a for a, b in it.pairwise(line)}
    print(diff)
    if diff <= {1, 2, 3} or diff <= {-1, -2 ,-3}:
        answer += 1

# 490
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))