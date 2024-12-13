import math
from functools import cache

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 11

answer = 0
# data = '''0 1 10 99 999'''
data = '''125 17'''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

stones = [int(i) for i in data.split()]
print(stones)

@cache
def rec(stone, amount=0):
    if amount == 75:
        return 1
    if stone == 0:
        return rec(1, amount + 1)
    li = math.floor(math.log10(stone)) + 1
    if li % 2 == 0:
        l1 = stone // 10 ** (li // 2)
        l2 = stone % 10 ** (li // 2)
        return rec(l1, amount + 1) + rec(l2, amount + 1)
    return rec(stone*2024, amount + 1)

for i in stones:
    print("chuj")
    answer += rec(i)
# answer = sum([rec(i) for i in stones])
    # print(n)
    # new_stones = []
    # for i in stones:
    #     if i == 0:
    #         new_stones.append(1)
    #         continue
    #     # li = math.floor(math.log10(i))+1
    #     # if li % 2 == 0:
    #     #     new_stones.append(li % 10**(li//2))
    #     #     new_stones.append(li // 10**(li//2))
    #     #     continue
    #     new_stones.append(i*2024)
    # stones = new_stones.copy()

# print(stones)
#
# answer = len(stones)

print(answer)
# pyperclip.copy(str(answer))