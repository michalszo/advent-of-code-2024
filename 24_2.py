from collections import defaultdict

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 24

answer = 0
# data = '''x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1
#
# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj'''
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

for gate in gates.items():
    ((a, b), op), c = gate
    if {a[1:], b[1:], c[1:]} & {"33"} or {a, b, c} & {"hgj"}:
        print(gate)

# # nnt <-> gws
# gates[(frozenset({'y09', 'x09'}), 'AND')], gates[(frozenset({'y09', 'x09'}), 'XOR')] = gates[(frozenset({'y09', 'x09'}), 'XOR')], gates[(frozenset({'y09', 'x09'}), 'AND')]
# # z13 <-> npf
# gates[(frozenset({'tqs', 'fmh'}), 'OR')], gates[(frozenset({'kvr', 'hgw'}), 'XOR')] = gates[(frozenset({'kvr', 'hgw'}), 'XOR')], gates[(frozenset({'tqs', 'fmh'}), 'OR')]
# # z19 <-> cph
# gates[(frozenset({'y19', 'x19'}), 'AND')], gates[(frozenset({'fnq', 'rsm'}), 'XOR')] = gates[(frozenset({'fnq', 'rsm'}), 'XOR')], gates[(frozenset({'y19', 'x19'}), 'AND')]
# # z33 <-> hgj
# gates[(frozenset({'wgq', 'wtm'}), 'AND')], gates[(frozenset({'wgq', 'wtm'}), 'XOR')] = gates[(frozenset({'wgq', 'wtm'}), 'XOR')], gates[(frozenset({'wgq', 'wtm'}), 'AND')]

indexes = [str(i).rjust(2, "0") for i in range(45)]

xors = {i: gates[(frozenset({"x"+i, "y"+i}), "XOR")] for i in indexes}
ands = {i: gates[(frozenset({"x"+i, "y"+i}), "AND")] for i in indexes}
print("X", xors)
print("A", ands)

part_carryovers = {} # {indexes[n]: (inp, out) for n in range(2, 45) for (inp, op), out in gates.items() if op == "AND" and xors[indexes[n-1]] in inp}
carryovers = {"01": (frozenset({"x00", "y00"}), ands["00"])} # | {indexes[n]: (inp, out) for n in range(2, 45) for (inp, op), out in gates.items() if op == "OR" and ands[indexes[n-1]] in inp}
# results = {} # {indexes[n]: (inp, out) for n in range(1, 45) for (inp, op), out in gates.items() if op == "XOR" and xors[indexes[n]] in inp}

print("P", part_carryovers)
print("C", carryovers)
# print("R", results)

swaps = set()

for n in range(2, 45):
    prev = indexes[n-1]
    index = indexes[n]
    print(index, swaps)
    pin, pout = [(inp, out) for (inp, op), out in gates.items() if op == "AND" and (xors[prev] in inp or carryovers[prev][1] in inp)][0]
    if xors[prev] not in pin:
        swaps |= {xors[prev]} | (pin - {carryovers[prev][1]})
    if carryovers[prev][1] not in pin:
        swaps |= {carryovers[prev][1]} | (pin - {xors[prev]})
    part_carryovers[index] = (pin, pout)
    cin, cout = [(inp, out) for (inp, op), out in gates.items() if op == "OR" and (ands[prev] in inp or part_carryovers[index][1] in inp)][0]
    carryovers[index] = (cin, cout)
    if ands[prev] not in cin:
        swaps |= {ands[prev]} | (cin - {part_carryovers[index][1]})
    if part_carryovers[index][1] not in cin:
        swaps |= {part_carryovers[index][1]} | (cin - {ands[prev]})

answer = ",".join(sorted(swaps))

# cph,gws,hgj,nnt,npf,z13,z19,z33
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))
