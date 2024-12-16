from copy import deepcopy

from string_formatting import print_formatted
from util import *
import itertools as it
import time

DAY = 15

answer = 0
# data = '''#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######
#
# <vv<<^^<<^^'''
# data = '''##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########
#
# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

def add_pos(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]

mapa, moves = [i.splitlines() for i in data.split("\n\n")]
mapa = [[*it.chain(*[j*2 if j != "O" else "[]" for j in i])] for i in mapa]
moves = "".join((it.chain(*moves)))
print(mapa, moves)

for y, row in enumerate(mapa):
    for x, v in enumerate(mapa[y]):
        if mapa[y][x] == "@":
            robot = (x, y)
            mapa[y][x] = "."
            mapa[y][x+1] = "."

assert robot is not None
print(robot)

# import pygame
# pygame.init()
#
# screen = pygame.display.set_mode((len(mapa[0]), len(mapa)))

for move in moves:
    # print("".join(["".join([j for j in i]) for i in mapa]).count('['))
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         exit(1)
    #     if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
    #         exit(1)
    # screen.fill(0)
    # pxarray = pygame.PixelArray(screen)
    # for y, row in enumerate(mapa):
    #     for x, v in enumerate(row):
    #         if v in ["[", "]"]:
    #             pxarray[x, y] = 0xFFFFFF
    #         if (x, y) == robot:
    #             pxarray[x, y] = 0x00FF00
    # pygame.display.set_caption(move)
    # pygame.display.flip()
    # time.sleep(0.05)

    # for y, row in enumerate(mapa):
    #     s = row.copy()
    #     if y == robot[1]:
    #         s[robot[0]] = "@"
    #     print("".join(s))
    # print(move)
    direction = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}[move]
    robot_newpos = add_pos(robot, direction)
    if mapa[robot_newpos[1]][robot_newpos[0]] == ".":
        robot = robot_newpos
        continue
    elif mapa[robot_newpos[1]][robot_newpos[0]] == "#":
        continue
    else:
        if direction[0]:
            if '.' not in mapa[robot[1]][robot[0] + direction[0]::direction[0]]:
                continue
            dist = mapa[robot[1]][robot[0] + direction[0]::direction[0]].index('.')
            bad_dist = mapa[robot[1]][robot[0] + direction[0]::direction[0]].index('#')
            if bad_dist < dist:
                continue
            first_space = robot[0] + direction[0] * (1 + dist)
            del mapa[robot[1]][first_space]
            if direction[0] == 1:
                mapa[robot[1]].insert(robot[0], '.')
            elif direction[0] == -1:
                mapa[robot[1]].insert(robot[0]-1, '.')
            robot = robot_newpos
        elif direction[1]:
            frontier = {robot_newpos}
            if mapa[robot_newpos[1]][robot_newpos[0]] == '[':
                frontier.add((robot_newpos[0] + 1, robot_newpos[1]))
            if mapa[robot_newpos[1]][robot_newpos[0]] == ']':
                frontier.add((robot_newpos[0] - 1, robot_newpos[1]))
            blocks_to_move = set()
            no_obstacles = True
            while frontier:
                # print(frontier)
                new_blocks = set()
                for block in frontier:
                    check_pos = (block[0], block[1] + direction[1])
                    # print(block, check_pos)
                    if mapa[check_pos[1]][check_pos[0]] == "[":
                        new_blocks.add(check_pos)
                        new_blocks.add((check_pos[0] + 1, check_pos[1]))
                    elif mapa[check_pos[1]][check_pos[0]] == "]":
                        new_blocks.add(check_pos)
                        new_blocks.add((check_pos[0] - 1, check_pos[1]))
                    elif mapa[check_pos[1]][check_pos[0]] == "#":
                        no_obstacles = False
                        break
                    # print(new_blocks)
                else:
                    blocks_to_move |= frontier
                    frontier = new_blocks.copy()
                    continue
                break
            if no_obstacles:
                # print(blocks_to_move)
                kopia_mapy = deepcopy(mapa)
                for x, y in blocks_to_move:
                    kopia_mapy[y][x] = '.'
                for x, y in blocks_to_move:
                    kopia_mapy[y+direction[1]][x] = mapa[y][x]
                mapa = deepcopy(kopia_mapy)
                robot = robot_newpos

for y, row in enumerate(mapa):
    s = row.copy()
    if y == robot[1]:
        s[robot[0]] = "@"
    print("".join(s))

for y, row in enumerate(mapa):
    for x, v in enumerate(mapa[y]):
        if mapa[y][x] == "[":
            print(x, y)
            answer += 100*y + x



print(answer)
# 1582876 too high
# pyperclip.copy(str(answer))