import re
import time
from collections import defaultdict
from functools import reduce

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 14

answer = 0
data = ''''''
# data = load_test_data(DAY); SIZE = (11, 7)
data = load_data(DAY); SIZE = (101, 103)
print_formatted(f"&e3&#ec{data}")

data = set(tuple(int(j) for j in re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", i).groups()) for i in data.splitlines())
print(data)

# for i in range(SIZE[0]*SIZE[1]):
#     if i % SIZE[0] == 2 and i % SIZE[1] == 76:
#         print(i)

i = 0
while 1:
    h_lines = defaultdict(set)
    for px, py, vx, vy in data:
        nx, ny = (px+i*vx) % SIZE[0], (py+i*vy) % SIZE[1]
        h_lines[ny].add(nx)
    longest_longest = 0
    for row in h_lines.values():
        ordered = sorted(row)
        longest = 0
        current = 0
        prev = None
        for n in ordered:
            if current == 0:
                prev = n
                current = 1
            else:
                if n == prev + 1:
                    prev = n
                    current += 1
                else:
                    prev = None
                    longest = max(longest, current)
                    current = 0
        longest_longest = max(longest_longest, longest)
    if longest_longest >= 14: # (7+21)/2
        answer = i
        break
        # print(i, longest_longest)
    i += 1

# i = 6668 # 2+101 76+103
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit(1)
#         if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
#             exit(1)
#     screen.fill(0)
#     pxarray = pygame.PixelArray(screen)
#     for px, py, vx, vy in data:
#         nx, ny = (px+i*vx) % SIZE[0], (py+i*vy) % SIZE[1]
#         pxarray[nx, ny] = 0xFFFFFF
#     pygame.display.set_caption(str(i))
#     pygame.display.flip()
#     i += 1
#     time.sleep(10.5)

# 6668
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))