import re
from functools import reduce

from PIL.ImageChops import add_modulo

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 3

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print(f"&e3&#ec{data}")
print()

data = data.replace("\r\n", "")
matches = re.findall(r"mul\((\d+),(\d+)\)", data)
print(matches)
answer = sum([int(a)*int(b) for a,b in matches])

print(answer)
# pyperclip.copy(str(answer))