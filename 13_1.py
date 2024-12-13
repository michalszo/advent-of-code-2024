import math
import re

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 13

answer = 0
data = ''''''
data = load_test_data(DAY)
# data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = [[int(j) for j in re.match(
    r'''Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)''', i).groups()] for i in data.split("\n\n")]

x_data = [i[::2] for i in data]
y_data = [i[1::2] for i in data]
print(x_data)
print(y_data)

for (a, b, target), (ya, yb, ytarget) in zip(x_data, y_data):
    min_cost = math.inf
    # a_count = target // a
    for a_count in range(target // a, -1, -1):
        b_count = (target - a_count*a) // b
        cost = 3*a_count + b_count
        if a*a_count + b*b_count == target and ya*a_count + yb*b_count == ytarget:
            min_cost = min(min_cost, cost)
            print(a, b, target, a_count, b_count, a*a_count + b*b_count, cost)
    # print(target - a_count*a)
    if not math.isinf(min_cost):
        answer += min_cost

print(answer)
# pyperclip.copy(str(answer))