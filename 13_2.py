from string_formatting import print_formatted
from util import *
import itertools as it
import re

DAY = 13

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [[int(j) for j in re.match(
    r'''Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)''', i).groups()] for i in data.split("\n\n")]

x_data = [i[::2] for i in data]
y_data = [i[1::2] for i in data]
print(x_data)
print(y_data)

for (a, b, target), (ya, yb, ytarget) in zip(x_data, y_data):
    target += 10000000000000
    ytarget += 10000000000000

    # xo, yo = set(), set()
    # xt, yt = b // math.gcd(a, b), yb // math.gcd(ya, yb)
    #
    # # print(xt, yt)
    #
    # for a_count in range(xt):
    #     b_count = (target - a_count * a) // b
    #     # print(a * a_count + b * b_count)
    #     if a * a_count + b * b_count == target:
    #         xo.add(a_count)
    #
    # for a_count in range(yt):
    #     b_count = (ytarget - a_count * ya) // yb
    #     # print(a_count, b_count)
    #     # print(a * a_count + b * b_count)
    #     if ya * a_count + yb * b_count == ytarget:
    #         yo.add(a_count)
    #
    # t = math.lcm(xt, yt)
    # o = {i for i in range(t) if i % xt in xo and i % yt in yo}
    #
    # # print(xt, xo, yt, yo, t, o)
    #
    # if not o:
    #     continue

    # min_cost = math.inf
    a_count = round((ytarget*b - target*yb)/(ya*b - a*yb))
    b_count = (target - a_count * a) // b
    # print(o, a_count % t)
    if a * a_count + b * b_count == target and ya * a_count + yb * b_count == ytarget:
        cost = 3 * a_count + b_count
        answer += cost
        print(cost)
    # if 3*a <= b:
    #     # FUNKCJA ROSNĄCA
    #     for i in o:
    #         a_count = i
    #         b_count = (target - a_count * a) // b
    #         print(a * a_count + b * b_count, ya * a_count + yb * b_count)
    #
    #     # the_range = range(target // a + 1, t)
    #     pass
    # else:
    #     # FUNKCJA MALEJĄCA
    #     for i in o:
    #         a_count = target // a // t * t + i
    #         b_count = (target - a_count * a) // b
    #         print(a * a_count + b * b_count, ya * a_count + yb * b_count)
    #     pass
        # the_range = range(target // a, -1, -t)
    # for a_count in the_range:
    #     b_count = (target - a_count * a) // b
    #     cost = 3 * a_count + b_count
    #     if a * a_count + b * b_count == target and ya * a_count + yb * b_count == ytarget:
    #         min_cost = cost
    #         print(a_count, b_count, cost)
    #         break
    # min_cost = math.inf
    # # a_count = target // a
    # for a_count in range(target // a, -1, -1):
    #     b_count = (target - a_count*a) // b
    #     cost = 3*a_count + b_count
    #     if a*a_count + b*b_count == target and ya*a_count + yb*b_count == ytarget:
    #         min_cost = min(min_cost, cost)
    #         print(a, b, target, a_count, b_count, a*a_count + b*b_count, cost)
    # # print(target - a_count*a)
    # if not math.isinf(min_cost):
    #     answer += min_cost

# 82261957837868
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))