from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 11

answer = 0
# data = '''0 1 10 99 999'''
# data = '''125 17'''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

stones = [int(i) for i in data.split()]
print(stones)

for _ in range(25):
    new_stones = []
    for i in stones:
        if i == 0:
            new_stones.append(1)
            continue
        li = math.floor(math.log10(i))+1
        if li % 2 == 0:
            l1 = i // 10**(li//2)
            l2 = i % 10**(li//2)
            new_stones.append(l1)
            new_stones.append(l2)
            continue
        new_stones.append(i*2024)
    stones = new_stones.copy()

print(stones)

answer = len(stones)

# 202019
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))