from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 15

answer = 0
data = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''
data = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

def add_pos(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]

mapa, moves = [i.splitlines() for i in data.split("\n\n")]
mapa = [[*i] for i in mapa]
moves = "".join((it.chain(*moves)))
print(mapa, moves)

for y, row in enumerate(mapa):
    for x, v in enumerate(mapa[y]):
        if mapa[y][x] == "@":
            robot = (x, y)
            mapa[y][x] = "."

assert robot is not None
print(robot)

for move in moves:
    direction = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}[move]
    robot_newpos = add_pos(robot, direction)
    if mapa[robot_newpos[1]][robot_newpos[0]] == "#":
        continue
    elif mapa[robot_newpos[1]][robot_newpos[0]] == "O":
        box_newpos = robot_newpos
        while 1:
            box_newpos = add_pos(box_newpos, direction)
            if mapa[box_newpos[1]][box_newpos[0]] == "#":
                break
            if mapa[box_newpos[1]][box_newpos[0]] == "O":
                continue
            if mapa[box_newpos[1]][box_newpos[0]] == ".":
                mapa[robot_newpos[1]][robot_newpos[0]] = "."
                mapa[box_newpos[1]][box_newpos[0]] = "O"
                robot = robot_newpos
                break
    elif mapa[robot_newpos[1]][robot_newpos[0]] == ".":
        robot = robot_newpos

for y, row in enumerate(mapa):
    for x, v in enumerate(mapa[y]):
        if mapa[y][x] == "O":
            answer += 100*y + x



print(answer)
# pyperclip.copy(str(answer))