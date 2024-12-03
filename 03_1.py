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

print_formatted(f"&e3&#ec{data}")


data = data.replace("\r\n", "")
print(data)

matches = re.findall(r"mul\(\d+,\d+\)", data)
print(matches)
for match in matches:
    a, b = match.replace("mul(", "").replace(")", "").split(",")
    print(a, b)
    answer += int(a)*int(b)
# answer = sum([ reduce(lambda a,b: a*b, [int(j) for j in ], 1) for i in matches])

print(answer)
# pyperclip.copy(str(answer))