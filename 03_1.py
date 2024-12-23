from string_formatting import print_formatted
from util import *
import itertools as it
import re

DAY = 3

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print(f"&e3&#ec{data}")

matches = re.findall(r"mul\((\d+),(\d+)\)", data)
print(matches)
answer = sum([int(a)*int(b) for a,b in matches])

# 178538786
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))