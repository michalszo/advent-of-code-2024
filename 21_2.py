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

koszty = {
    "<>": 3,
    "<^": 3,
    "<v": 2,
    "<A": 4,
    ">^": 3,
    ">v": 2,
    ">A": 2,
    "^v": 2,
    "^A": 2,
    "vA": 3,
}

for _ in range(1):
    v1, v2, v3, v4, v6 = koszty["<^"], koszty["<v"], koszty["<A"], koszty[">^"], koszty[">A"]
    koszty = {
        "<>": v6+1+1,
        "<^": v6+v4+1,
        "<v": v6+1,
        "<A": v6+1+v4+1,
        ">^": v3+v1+1,
        ">v": v3+1,
        ">A": v2+1,
        "^v": v1+1,
        "^A": v6+1,
        "vA": v6+v4+1,
    }
print(koszty)

napisy = [
    (29, ("<", "^", "^^>", "vvv")),
    (980, ("^^^", "<", "vvv", ">")),
    (179, ("^<<", "^^", ">>", "vvv")),
    (456, ("^^<<", ">", ">", "vv")),
    (379, ("^", "<<^^", ">>", "vvv")),
]

# napisy = [
#     (805, ("^^^<", "vvv", "^^", ">vv")),
#     (964, ("^^^", "v", "<<", ">>vv")),
#     (459, ("^^<<", ">", ">^", "vvv")),
#     (968, ("^^^", "v", "<^", ">vvv")),
#     (671, ("^^", "<<^", "vv", ">>v")),
# ]

# data = "^^^A<AvvvA>A"

def zrob(parametr):
    _wynik = 0
    for _a, _b in it.pairwise(f'A{parametr}'):
        if _a == _b:
            p = 1
        if _a != _b:
            if f'{_a}{_b}' in koszty.keys():
                p = koszty[f'{_a}{_b}']
            elif f'{_b}{_a}' in koszty.keys():
                p = koszty[f'{_b}{_a}']
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
# 295072 too high
# 276852 too low
# 275062 too low