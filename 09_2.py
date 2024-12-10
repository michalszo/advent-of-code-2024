import sys
from collections import defaultdict

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
if len(space) < len(files):
    space.append(0)

print(files, space)

moved = defaultdict(list)
# gaps = [(0, files[0])]

for right_id in range(len(files)-1, 0, -1):
    if not files[right_id]:
        continue
    for left_id in range(right_id):
        if space[left_id] >= files[right_id]:
            space[left_id] -= files[right_id]
            # if space[left_id] == 0:
            #     gaps[left_id].append(left_id + 1)
            moved[left_id].append(right_id)
            break
    # else:
    #     for left_id in range(right_id):
    #         if space[left_id] != 0:
    #             result.append((-1, space[left_id]))
    #             space[left_id] = 0
    #             break
moved = [moved[i] for i in range(len(files))]
print(moved)
print(space)


used = set()
n = 0
for i in range(len(files)):
    if i not in used:
        for _ in range(files[i]):
            print(i, end="")
            answer += n*i
            n += 1
    else:
        print("." * files[i], end="")
        n += files[i]
    used.add(i)
    for j in moved[i]:
        used.add(j)
        for _ in range(files[j]):
            print(j, end="")
            answer += n * j
            n += 1
    print("."*space[i], end="")
    n += space[i]
    # print(i, moved[i], space[i])
# unused = set(range(len(files)))
# while unused:
#     break

# while 1:
#     for i in range(len(files)-1, left_id, -1):
#         if files[i] <= space[left_id] and files[i] != 0:
#             result.append((i, files[i]))
#             print(result)
#             space[left_id] -= files[i]
#             files[i] = 0
#         while space[left_id] == 0:
#             left_id += 1
#             print(space)
    # break

print(answer)
# pyperclip.copy(str(answer))