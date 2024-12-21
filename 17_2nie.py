import re

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 17

answer = 0
data = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''
data = '''Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0'''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = re.match(r'''Register A: (\d+)
Register B: (\d+)
Register C: (\d+)

Program: ([\d,]+)''', data).groups()
# print(data)

reg = {
    "A": int(data[0]),
    "B": int(data[1]),
    "C": int(data[2]),
}

# program = list(it.batched([int(i) for i in data[3].split(",")], 2))
program = [int(i) for i in data[3].split(",")]

print(reg, program)

for A in range(10):
    reg = {
        "A": A,
        "B": int(data[1]),
        "C": int(data[2]),
    }
    pointer = 0

    outputs = []
    while 1:
        if pointer + 1 >= len(program):
            break
        opcode, literal = program[pointer:pointer+2]
        if 4 <= literal <= 6:
            combo = reg["ABC"[literal-4]]
        else:
            combo = literal
        # print(pointer, reg, opcode, literal, combo)
        if opcode == 0:
            reg["A"] //= (2**combo)
            print('reg["A"] //= (2**combo)', literal)
        elif opcode == 1:
            reg["B"] ^= literal
            print('reg["B"] ^= literal', literal)
        elif opcode == 2:
            reg["B"] = combo % 8
            print('reg["B"] = combo % 8', literal)
        elif opcode == 3:
            print('pointer = literal', literal)
            if reg["A"] != 0:
                pointer = literal
                pointer -= 2 # cancelling
        elif opcode == 4:
            reg["B"] ^= reg["C"]
            print('reg["B"] ^= reg["C"]', literal)
        elif opcode == 5:
            outputs.append(combo % 8)
            print('outputs.append(combo % 8)', literal)
        elif opcode == 6:
            reg["B"] = reg["A"] // (2**combo)
            print('reg["B"] = reg["A"] // (2**combo)', literal)
        elif opcode == 7:
            reg["C"] = reg["A"] // (2**combo)
            print('reg["C"] = reg["A"] // (2**combo)', literal)
        pointer += 2
    print(A, outputs)

print(reg)

answer = ",".join([str(i) for i in outputs])
# 4,4,1,1,5,6,6,6,6 nie

print(answer)
# pyperclip.copy(str(answer))