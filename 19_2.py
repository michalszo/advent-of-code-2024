from functools import cache

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 19

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

words, sentences = data.split("\n\n")
words = words.split(", ")
sentences = sentences.splitlines()

print(words, sentences)

@cache
def rec(s):
    if not s:
        return 1
    count = 0
    ok = [word for word in words if s.startswith(word)]
    for word in ok:
        # print(s, word)
        new_s = s[len(word):]
        count += rec(new_s)
    return count

for sentence in sentences:
    x = rec(sentence)
    print(x)
    answer += x

print(answer)
# pyperclip.copy(str(answer))