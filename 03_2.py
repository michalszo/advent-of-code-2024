import re
from functools import reduce

from PIL.ImageChops import add_modulo

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 3

answer = 0
data = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
# data = load_test_data(DAY)
data = load_data(DAY)

print(f"&e3&#ec{data}")


data = data.replace("\r\n", "")
print(data)

matches = re.findall(r"(don't\(\)|do\(\)|mul\(\d+,\d+\))", data)
print(matches)
enabled = True
for match in matches:
    if match == "don't()":
        enabled = False
    elif match == "do()":
        enabled = True
    elif enabled:
        a, b = match.replace("mul(", "").replace(")", "").split(",")
        print(a, b)
        answer += int(a)*int(b)

print(answer)
# pyperclip.copy(str(answer))