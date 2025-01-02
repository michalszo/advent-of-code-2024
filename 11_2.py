from string_formatting import print_formatted
from util import *
import itertools as it
from functools import cache

DAY = 11

answer = 0
# data = '''0 1 10 99 999'''
# data = '''125 17'''
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
    answer += rec(i)

# 239321955280205
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))