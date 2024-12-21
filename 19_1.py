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

def rec(s):
    if s in words:
        return 1

    ok = [word for word in words if s.startswith(word)]
    for word in ok:
        new_s = s[len(word):]
        if rec(new_s):
            return True
    return False

for sentence in sentences:
    if rec(sentence):
        answer += 1

print(answer)
# pyperclip.copy(str(answer))