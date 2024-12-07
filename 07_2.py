from functools import reduce

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
    for ops in it.product(range(3), repeat=len(numbers)-1):
        val = numbers[0]
        for n, op in zip(numbers[1:], ops):
            if op == 2:
                val = int(str(val) + str(n))
            elif op == 1:
                val *= n
            else:
                val += n
        if val == result:
            answer += result
            break

print(answer)
# pyperclip.copy(str(answer))