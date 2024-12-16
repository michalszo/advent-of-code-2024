import re
import time
from collections import defaultdict
from functools import reduce

from string_formatting import print_formatted
from util import *
import itertools as it

import pygame

DAY = 14

answer = 0
data = ''''''
# data = load_test_data(DAY); SIZE = (11, 7)
data = load_data(DAY); SIZE = (101, 103)

print_formatted(f"&e3&#ec{data}")

data = set(tuple(int(j) for j in re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", i).groups()) for i in data.splitlines())
print(data)

import pygame
pygame.init()

screen = pygame.display.set_mode(SIZE)

for i in range(SIZE[0]*SIZE[1]):
    if i % SIZE[0] == 2 and i % SIZE[1] == 76:
        print(i)

i = 6668 # 2+101 76+103
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            exit(1)
    screen.fill(0)
    pxarray = pygame.PixelArray(screen)
    for px, py, vx, vy in data:
        nx, ny = (px+i*vx) % SIZE[0], (py+i*vy) % SIZE[1]
        pxarray[nx, ny] = 0xFFFFFF
    pygame.display.set_caption(str(i))
    pygame.display.flip()
    i += 1
    time.sleep(1.5)