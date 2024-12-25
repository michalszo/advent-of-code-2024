from collections import defaultdict

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
gates = [tuple(i.split()) for i in gates.splitlines()]
gates = {(frozenset({i[0], i[2]}), i[1]): i[4] for i in gates}
print(values)
print(gates)

x_val = {(k, v) for k, v in values if k.startswith("x")}
x_val = sorted(x_val, key=lambda i: i[0])
x_val = "".join([str(v) for k, v in x_val])[::-1]

y_val = {(k, v) for k, v in values if k.startswith("y")}
y_val = sorted(y_val, key=lambda i: i[0])
y_val = "".join([str(v) for k, v in y_val])[::-1]

print("", x_val)
print("", y_val)
real_sum = bin(int(x_val, 2) + int(y_val, 2))[2:]
print(real_sum)
print(bin(42049478636360)[2:])

for gate in gates.items():
    ((a, b), op), c = gate
    if {a[1:], b[1:], c[1:]} & {"33"} or {a, b, c} & {"hgj"}:
        print(gate)

# nnt <-> gws
gates[(frozenset({'y09', 'x09'}), 'AND')], gates[(frozenset({'y09', 'x09'}), 'XOR')] = gates[(frozenset({'y09', 'x09'}), 'XOR')], gates[(frozenset({'y09', 'x09'}), 'AND')]
# z13 <-> npf
gates[(frozenset({'tqs', 'fmh'}), 'OR')], gates[(frozenset({'kvr', 'hgw'}), 'XOR')] = gates[(frozenset({'kvr', 'hgw'}), 'XOR')], gates[(frozenset({'tqs', 'fmh'}), 'OR')]
# z19 <-> cph
gates[(frozenset({'y19', 'x19'}), 'AND')], gates[(frozenset({'fnq', 'rsm'}), 'XOR')] = gates[(frozenset({'fnq', 'rsm'}), 'XOR')], gates[(frozenset({'y19', 'x19'}), 'AND')]
# z33 <-> hgj
gates[(frozenset({'wgq', 'wtm'}), 'AND')], gates[(frozenset({'wgq', 'wtm'}), 'XOR')] = gates[(frozenset({'wgq', 'wtm'}), 'XOR')], gates[(frozenset({'wgq', 'wtm'}), 'AND')]

print(",".join(sorted({"nnt", "gws", "z13", "npf", "z19", "cph", "z33", "hgj"})))

indexes = [str(i).rjust(2, "0") for i in range(45)]

xors = {i: gates[(frozenset({"x"+i, "y"+i}), "XOR")] for i in indexes}
ands = {i: gates[(frozenset({"x"+i, "y"+i}), "AND")] for i in indexes}
print("X", xors)
print("A", ands)

carryovers = {"01": ands["00"]}
part_carryovers = {}
# results = {"00": xors["00"], "01": gates[(frozenset({xors["01"], carryovers["01"]}), "XOR")]}
# print(results)

for n in range(2, 45):
    print("P", part_carryovers)
    print("C", carryovers)
    prev = indexes[n-1]
    index = indexes[n]
    part_carryovers[index] = gates[(frozenset({carryovers[prev], xors[prev]}), "AND")]
    carryovers[index] = gates[(frozenset({ands[prev], part_carryovers[index]}), "OR")]
    v = gates[(frozenset({xors[index], carryovers[index]}), "XOR")]
    if v != "z" + index:
        raise BaseException(f"z{index} != {v}")

# wrong_indexes = {i for i, (a, b) in enumerate(zip(real_sum[::-1], result[::-1])) if a != b}
# wrong_indexes = {33, 34, 35, 36, 37, 38, 9, 10, 13, 14, 19, 20, 21, 22}
#
# suspects = set()
#
# for gate in gates:
#     if {ii(gate[0][1:]), ii(gate[2][1:]), ii(gate[4][1:])} & wrong_indexes:
#         suspects.add(gate)
#
# print(len(suspects), sorted(suspects))

print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))
