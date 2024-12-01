from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 1

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = [[int(j) for j in i.split("   ")] for i in data.splitlines()]

l1 = []
l2 = []

for a1, a2 in data:
    l1.append(a1)
    l2.append(a2)

l1.sort()
l2.sort()

for a1, a2 in zip(l1, l2):
    answer += a1 * l2.count(a1)

print(answer)
# pyperclip.copy(str(answer))