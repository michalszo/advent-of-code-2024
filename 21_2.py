import itertools as it
import math

# from string_formatting import print_formatted
# from util import *
#
# DAY = 21
#
answer = 0
# data = ''''''
# data = load_test_data(DAY)
# # data = load_data(DAY)
#
# print_formatted(f"&e3&#ec{data}")
#
# data = [i for i in data.splitlines()]
# print(data)
#
# print(answer)
# # pyperclip.copy(str(answer))

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

napisy = [
    (29, ("<", "^", "^^>", "vvv")),
    (980, ("^^^", "<", "vvv", ">")),
    (179, ("^<<", "^^", ">>", "vvv")),
    (456, ("^^<<", ">", ">", "vv")),
    (379, ("^", "<<^^", ">>", "vvv")),
]

napisy = [
    (805, ("^^^<", "vvv", "^^", ">vv")),
    (964, ("^^^", "v", "<<", ">>vv")),
    (459, ("^^<<", ">", ">^", "vvv")),
    (968, ("^^^", "v", "<^", ">vvv")),
    (671, ("^^", "<<^", "vv", ">>v")),
]

def zrob(parametr):
    _wynik = 0
    for _a, _b in it.pairwise(f'A{parametr}'):
        _a = "<v^>A".index(_a)
        _b = "<v^>A".index(_b)
        p = t[_a][_b]
        _wynik += p
        # print(a, b, len(p), p)

    return _wynik

for kod, (a, b, c, d) in napisy:
    najlepszy_wynik = math.inf

    for (wa, wb, wc, wd) in it.product({-1, 1}, repeat=4):
        napis = f'{a[::wa]}A{b[::wb]}A{c[::wc]}A{d[::wd]}A'

        if napis.startswith("<<"):
            continue

        if napis.endswith(">>A"):
            continue

        wynik = zrob(napis)

        najlepszy_wynik = min(wynik, najlepszy_wynik)
    # print(len(jeden), jeden)
    # dwa = zrob(najlepszy_wynik)
    # print(dwa)
    q = kod*najlepszy_wynik
    print(kod, najlepszy_wynik, q)
    answer += q

print(answer)