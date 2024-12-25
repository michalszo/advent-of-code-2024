from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 24

answer = 0
data = '''x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
'''
# data = load_test_data(DAY)
data = load_data(DAY)
print_formatted(f"&e3&#ec{data}")

values, gates = data.split("\n\n")
values = [i.split(": ") for i in values.splitlines()]
values = [(i[0], int(i[1])) for i in values]
gates = [i.split() for i in gates.splitlines()]
print(values)
print(gates)

# values = []
# for n in range(45):
#     values += [("x" + str(n).rjust(2, "0"), 1), ("y" + str(n).rjust(2, "0"), 1)]
# # values = list([( for n in range(45))]) + list([(("y" + str(n).rjust(2, "0"), 0) for n in range(45))])
# print(values)

new_values = dict(values.copy())

while gates:
    gate = gates.pop(0)
    a, op, b, c = gate[0], gate[1], gate[2], gate[4]
    if a not in new_values.keys() or b not in new_values.keys():
        gates.append(gate)
        continue
    if op == "AND":
        new_values[c] = new_values[a] & new_values[b]
    elif op == "OR":
        new_values[c] = new_values[a] | new_values[b]
    elif op == "XOR":
        new_values[c] = new_values[a] ^ new_values[b]

result = {(k, v) for k, v in new_values.items() if k.startswith("z")}
result = sorted(result, key=lambda i: i[0])
result = "".join([str(v) for k, v in result])[::-1]
answer = int(result, 2)

print(result)

# 42049478636360
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))