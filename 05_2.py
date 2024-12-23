from string_formatting import print_formatted
from util import *
import itertools as it
from functools import cmp_to_key

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
    sorted_page = tuple(sorted(page, key=cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))))
    if sorted_page != page:
        answer += sorted_page[len(sorted_page) // 2]

# 4713
print_formatted(f"&ffAnswer: &e2{answer}")
# pyperclip.copy(str(answer))