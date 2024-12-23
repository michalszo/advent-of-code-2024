from string_formatting import print_formatted
from util import *
import itertools as it
import re

DAY = 3

answer = 0
data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
# data = load_test_data(DAY)
data = load_data(DAY)
print(f"&e3&#ec{data}")

matches = re.findall(r"(don't\(\)|do\(\)|mul\(\d+,\d+\))", data)
print(matches)
enabled = True
for match in matches:
    if match == "don't()":
        enabled = False
    elif match == "do()":
        enabled = True
    elif enabled:
        a, b = [int(i) for i in re.match(r"mul\((\d+),(\d+)\)", match).groups()]
        print(a, b)
        answer += a * b

# 102467299
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))