from string_formatting import print_formatted
from util import *
import itertools as it
import math


DAY = 21

answer = 0
# data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [i for i in data.splitlines()]
print(data)

t = [
    [1, 2, 3, 3, 4],
    [2, 1, 2, 2, 3],
    [2, 2, 1, 3, 2],
    [3, 2, 3, 1, 2],
    [4, 3, 2, 2, 1],
]

for _ in range(24):
    t = [
        [1, t[4][3]+t[3][4], t[4][3]+t[3][2]+t[2][4], t[4][3]+1+t[3][4], t[4][3]+1+t[3][2]+t[2][4]],
        [t[4][0]+t[0][4], 1, t[4][2]+t[2][4], t[4][3]+t[3][4], t[4][2]+t[2][3]+t[3][4]],
        [t[4][1]+t[1][0]+t[0][4], t[4][1]+t[1][4], 1, t[4][1]+t[1][3]+t[3][4], t[4][3]+t[3][4]],
        [t[4][0]+1+t[0][4], t[4][0]+t[0][4], t[4][0]+t[0][2]+t[2][4], 1, t[4][2]+t[2][4]],
        [t[4][1]+t[1][0]+1+t[0][4], t[4][0]+t[0][1]+t[1][4], t[4][0]+t[0][4], t[4][1]+t[1][4], 1],
    ]
print(t)

pad = "789\n456\n123\n 0A"

codes = []
for i in data:
    moves = []
    for a, b in zip("A" + i, i):
        step = ""
        ax, ay = pad.index(a) % 4, pad.index(a) // 4
        bx, by = pad.index(b) % 4, pad.index(b) // 4
        dx = bx - ax
        dy = by - ay
        if dx < 0:
            step += "<"*-dx
        if dx > 0:
            step += ">"*dx
        if dy < 0:
            step += "^"*-dy
        if dy > 0:
            step += "v"*dy
        moves.append(step)
    codes.append((i, moves))

print(codes)

def do(parametr):
    outcome = 0
    for _a, _b in it.pairwise(f'A{parametr}'):
        _a = "<v^>A".index(_a)
        _b = "<v^>A".index(_b)
        p = t[_a][_b]
        outcome += p
        # print(a, b, len(p), p)

    return outcome

for code, (a, b, c, d) in codes:
    best_result = math.inf

    for (wa, wb, wc, wd) in it.product({-1, 1}, repeat=4):
        string = f'{a[::wa]}A{b[::wb]}A{c[::wc]}A{d[::wd]}A'

        if string.startswith("<<"):
            continue

        if string.endswith(">>A"):
            continue

        result = do(string)

        best_result = min(result, best_result)
    q = int(code[:-1]) * best_result
    print(code, best_result, q)
    answer += q

# 337744744231414
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))