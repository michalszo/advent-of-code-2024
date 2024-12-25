from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 25

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [i.splitlines() for i in data.split("\n\n")]
print(data)

locks = set()
keys = set()

for i in data:
    print(i)
    ls = []
    for x in range(len(i[0])):
        l = -1
        for y in range(len(i)):
            if i[y][x] == "#":
                l += 1
        ls.append(l)
    if "#" in i[0]:
        locks.add(tuple(ls))
    else:
        keys.add(tuple(ls))
    # keys.append([len(i)-1-j-1 for j in ls])
    # if len(i)//2 not in ls:
    #     answer += 1
    # print(ls)

print(locks)
print(keys)

for a, b in it.product(locks, keys):
    # b = [5-i for i in b]
    if False not in [x+y<=5 for x, y in zip(a, b)]:
        print(a, b)
        answer += 1
# print(keys)

print_formatted(f"&ffAnswer: &e2{answer}")
# nie 6426, 6171
# pyperclip.copy(str(answer))