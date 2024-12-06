from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 5

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

rules, pages = data.split("\n\n")
rules = [[int(j) for j in i.split("|")] for i in rules.splitlines()]
pages = [[int(j) for j in i.split(",")] for i in pages.splitlines()]
print(rules, pages)

# befores = {}
# afters = {}
# for n in range(100):
#     before = {n}
#     after = {n}
#     changes = True
#     while changes:
#         changes = False
#         for first, second in rules:
#             for i in before.copy():
#                 if i == second and first not in before:
#                     before.add(first)
#                     changes = True
#             for i in after.copy():
#                 if i == first and second not in after:
#                     after.add(second)
#                     changes = True
#     befores[n] = before
#     afters[n] = after
#
# print(befores)

for page in pages:
    for a, b in it.combinations(page, 2):
        if [b, a] in rules:
            break
    #     if (b in befores[a] and b not in afters[a]) or (a in afters[b] and not a in befores[b]):
    #         print(page, a, b)
    #         break
    else:
        answer += page[len(page) // 2]
        # print(a, b)

print(answer)
# 11979 nie
# pyperclip.copy(str(answer))