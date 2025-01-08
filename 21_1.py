from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 21

answer = 0
# data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = [i for i in data.splitlines()]
print(data)


translate = {
    "<>": (">>", "<<"),
    "<^": (">^", "v<"),
    "<v": (">", "<"),
    "<A": (">>^", "v<<"),
    ">^": ("<^", "v>"),
    ">v": ("<", ">"),
    ">A": ("^", "v"),
    "^v": ("v", "^"),
    "^A": (">", "<"),
    "vA": (">^", "v<"),
}

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

def do(parameter):
    outcome = ""
    for _a, _b in it.pairwise(f'A{parameter}'):
        if _a == _b:
            p = "A"
        if _a != _b:
            if f'{_a}{_b}' in translate.keys():
                p = translate[f'{_a}{_b}'][0] + "A"
            elif f'{_b}{_a}' in translate.keys():
                p = translate[f'{_b}{_a}'][1] + "A"
        outcome += p
        # print(a, b, len(p), p)

    return outcome

for code, (a, b, c, d) in codes:
    best_result = ""

    for (wa, wb, wc, wd) in it.product({-1, 1}, repeat=4):
        string = f'{a[::wa]}A{b[::wb]}A{c[::wc]}A{d[::wd]}A'

        if string.startswith("<<"):
            continue

        if string.endswith(">>A"):
            continue

        result = do(do(string))

        if not best_result or len(result) <= len(best_result):
            best_result = result
    q = int(code[:-1]) * len(best_result)
    print(code, len(best_result), q)
    answer += q

# 278748
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))