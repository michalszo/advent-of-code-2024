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


def check_page(_page):
    for a, b in it.combinations(_page, 2):
        if [b, a] in rules:
            na, nb = _page.index(b), _page.index(a)
            _page[na] = a
            _page[nb] = b
            return check_page(_page)
    return _page

for page in pages:
    ordered_page = check_page(page.copy())
    if ordered_page != page:
        answer += ordered_page[len(ordered_page) // 2]
print(answer)
# 11979 nie
# pyperclip.copy(str(answer))