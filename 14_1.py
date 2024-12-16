import re
from collections import defaultdict
from functools import reduce

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 14

answer = 0
data = ''''''
# data = load_test_data(DAY); SIZE = (11, 7)
data = load_data(DAY); SIZE = (101, 103)

print_formatted(f"&e3&#ec{data}")

data = [[int(j) for j in re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", i).groups()] for i in data.splitlines()]
print(data)

qs = defaultdict(int)
for px, py, vx, vy in data:
    nx, ny = (px+100*vx) % SIZE[0], (py+100*vy) % SIZE[1]
    q = (nx - SIZE[0] // 2, ny - SIZE[1] // 2)
    # print(nx, ny, q)
    if q[0] == 0 or q[1] == 0:
        continue
    q = (q[0] > 0, q[1] > 0)
    qs[q] += 1
print(qs)
answer = reduce(lambda a, b: a * b, qs.values())

print(answer)
# nie 94154500
# nie 223121256
# pyperclip.copy(str(answer))