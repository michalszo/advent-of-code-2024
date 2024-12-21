import itertools as it
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

tlumacz = {
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
    wynik = ""
    for _a, _b in it.pairwise(f'A{parametr}'):
        if _a == _b:
            p = "A"
        if _a != _b:
            if f'{_a}{_b}' in tlumacz.keys():
                p = tlumacz[f'{_a}{_b}'][0] + "A"
            elif f'{_b}{_a}' in tlumacz.keys():
                p = tlumacz[f'{_b}{_a}'][1] + "A"
        wynik += p
        # print(a, b, len(p), p)

    return wynik

for kod, (a, b, c, d) in napisy:
    najlepszy_wynik = ""

    for (wa, wb, wc, wd) in it.product({-1, 1}, repeat=4):
        napis = f'{a[::wa]}A{b[::wb]}A{c[::wc]}A{d[::wd]}A'

        if napis.startswith("<<"):
            continue

        if napis.endswith(">>A"):
            continue

        nie_wynik = zrob(napis)
        wynik = nie_wynik#zrob(nie_wynik)

        # print(napis, len(wynik))

        if not najlepszy_wynik or len(wynik) <= len(najlepszy_wynik):
            najlepszy_wynik = wynik
    # print(len(jeden), jeden)
    # dwa = zrob(najlepszy_wynik)
    # print(dwa)
    q = kod*len(najlepszy_wynik)
    print(kod, len(najlepszy_wynik), q)
    answer += q

print(answer)
# 295072 too high
# 276852 too low
# 275062 too low

print(zrob(zrob("v<A")))
print(zrob(zrob("<vA")))