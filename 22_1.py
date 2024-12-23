from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 22

answer = 0
data = ''''''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = [int(i) for i in data.splitlines()]
print(data)

for secret in data:
    for _ in range(2000):
        secret ^= (secret<<6)
        secret %= (2**24)
        secret ^= (secret>>5)
        secret %= (2**24)
        secret ^= (secret<<11)
        secret %= (2**24)
    print(secret)
    answer += secret

print(answer)
# pyperclip.copy(str(answer))