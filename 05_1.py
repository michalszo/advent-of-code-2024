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
rules = frozenset(tuple(int(j) for j in i.split("|")) for i in rules.splitlines())
pages = frozenset(tuple(int(j) for j in i.split(",")) for i in pages.splitlines())
print(rules)
print(pages)

for page in pages:
    for a, b in it.combinations(page, 2):
        if (b, a) in rules:
            break
    else:
        answer += page[len(page) // 2]
        # print(a, b)

# 7307
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))