from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 1

answer = 0
data = ''''''
data = load_test_data(DAY)
# data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [i for i in data.splitlines()]
print(data)

print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))