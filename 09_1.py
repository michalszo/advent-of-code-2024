import sys

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 9

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

sys.set_int_max_str_digits(20000)

print_formatted(f"&e3&#ec{data}")

files = [int(i) for i in data[::2]]
space = [int(i) for i in data[1::2]]

print(files, space)

left_id = 0
right_id = len(files) - 1

n = 0
while 1:
    while files[left_id]:
        files[left_id] -= 1
        print(left_id, end="")
        answer += n*left_id
        n += 1
    while space[left_id]:
        if not files[right_id]:
            right_id -= 1
            if left_id >= right_id:
                break
        space[left_id] -= 1
        files[right_id] -= 1
        print(right_id, end="")
        answer += n*right_id
        n += 1
    left_id += 1
    if left_id >= right_id:
        break

for i, s in enumerate(files):
    if s:
        for _ in range(s):
            print(i, end="")
            answer += n*i
            n += 1
print()

print(answer)
# pyperclip.copy(str(answer))