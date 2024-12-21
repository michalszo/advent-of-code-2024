import itertools as it
import math

# program = (2,4,1,5,7,5,1,6,4,2,5,5,0,3,3,0)
#
# git = range(1024)
# for n in range(15):
#     nowe_git = set()
#     for base in git:
#         for A in range(base*8, base*8+8):
#             # out =
#             out = ((((A%8)^5)^6)^(A//(2**((A%8)^5)))) % 8
#
#             if out == program[15-n]:
#                 nowe_git.add(A)
#     git = nowe_git.copy()
# print(git)
# print(min(git))

# 13427108806931 too low

# def inv(_v):
#     return "1" if _v == "0" else "0"
#
#
# patterns = []
#
# for n, v in enumerate(program):
#     bits = bin(v)[2:].rjust(3, "0")
#     patterns.append([i.replace("x", bits[0]) for i in [
#     f'..{bits[0]}{inv(bits[1])}{inv(bits[2])}..000' + '...'*n,
#     f'...{bits[0]}{inv(bits[1])}{bits[2]}.001' + '...'*n,
#     f'{bits[0]}{bits[1]}{inv(bits[2])}....010' + '...'*n,
#     f'.{bits[0]}{bits[1]}{bits[2]}...011' + '...'*n,
#     f'......{inv(bits[0])}010' + '...'*n,
#     f'.......011' + '...'*n,
#     f'....{inv(bits[0])}{bits[1]}{inv(bits[2])}110' + '...'*n,
#     f'.....{inv(bits[0])}{bits[1]}111' + '...'*n,
#     ]])
# print(patterns)
#
# while len(patterns) > 1:
#     compatible = set()
#     for a, b in it.product(patterns[0], patterns[1]):
#         new_reversed = ""
#         for x, y in it.zip_longest(a[::-1], b[::-1], fillvalue="."):
#             if x != "." and y != "." and x != y:
#                 break
#             elif x == "0" or y == "0":
#                 new_reversed += "0"
#             elif x == "1" or y == "1":
#                 new_reversed += "1"
#             else:
#                 new_reversed += "."
#         else:
#             compatible.add(new_reversed[::-1])
#     del patterns[0]
#     patterns[0] = compatible
#     print(len(patterns), len(compatible))
#
# open("17compatible.txt", "w+").writelines([i+"\n" for i in compatible])

best = math.inf

# data = open("17compatible.txt", "r+").read().strip().splitlines()
# print(data)

for i in open("17compatible.txt", "r+").read().strip().splitlines():
    print(int(i.replace(".", "0"), 2))
    best = min(best, int(i.replace(".", "0"), 2))

print(best)

# print(compatible)
    # break
        # print("   "+a)
        # print(b)
        # print()