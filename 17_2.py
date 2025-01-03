from string_formatting import print_formatted
from util import *
import itertools as it
import re

DAY = 17

answer = 0
# data = '''Register A: 729
# Register B: 0
# Register C: 0
#
# Program: 0,1,5,4,3,0'''
# data = '''Register A: 0
# Register B: 2024
# Register C: 43690
#
# Program: 4,0'''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

data = re.match(r'''Register A: (\d+)
Register B: (\d+)
Register C: (\d+)

Program: ([\d,]+)''', data).groups()

program = [int(i) for i in data[3].split(",")]

def run(_A):
    reg = {
        "A": _A,
        "B": int(data[1]),
        "C": int(data[2]),
    }
    pointer = 0
    outputs = []
    while 1:
        if pointer + 1 >= len(program):
            break
        opcode, literal = program[pointer:pointer + 2]
        if 4 <= literal <= 6:
            combo = reg["ABC"[literal - 4]]
        else:
            combo = literal
        # print(pointer, reg, opcode, literal, combo)
        if opcode == 0:
            reg["A"] //= (2 ** combo)
        elif opcode == 1:
            reg["B"] ^= literal
        elif opcode == 2:
            reg["B"] = combo % 8
        elif opcode == 3:
            if reg["A"] != 0:
                pointer = literal
                pointer -= 2  # cancelling
        elif opcode == 4:
            reg["B"] ^= reg["C"]
        elif opcode == 5:
            outputs.append(combo % 8)
        elif opcode == 6:
            reg["B"] = reg["A"] // (2 ** combo)
        elif opcode == 7:
            reg["C"] = reg["A"] // (2 ** combo)
        pointer += 2
    return outputs

ok = {n for n in range(2**10) if run(n)[-1] == program[-1]}
for i in range(-2, -len(program)-1, -1):
    new_ok = set()
    for n in ok:
        for A in range(n*8, (n+1)*8):
            r = run(A)
            assert r[-1] == program[-1]
            if r[i] == program[i]:
                new_ok.add(A)
    ok = new_ok.copy()
    print(i, len(ok))
    # print(A, run(A))

answer = min(ok)

# 107416870455451
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))