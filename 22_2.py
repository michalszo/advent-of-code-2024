from collections import defaultdict
from email.policy import default

from string_formatting import print_formatted
from util import *
import itertools as it

DAY = 22

answer = 0
data = '''1
2
3
2024'''
# data = load_test_data(DAY)
data = load_data(DAY)

print_formatted(f"&e3&#ec{data}")

data = [int(i) for i in data.splitlines()]
print(data)

seqs = defaultdict(int)

for secret in data:
    # print(".", secret)
    seq = []
    prev = secret % 10
    used = set()
    for _ in range(2000):
        secret ^= (secret << 6)
        secret %= (2 ** 24)
        secret ^= (secret >> 5)
        secret ^= (secret << 11)
        secret %= (2 ** 24)
        seq.append((secret % 10) - prev)
        prev = secret % 10
        if len(seq) >= 4:
            k = tuple(seq[-4:])
            if k not in used:
                seqs[tuple(seq[-4:])] += secret % 10
                used.add(k)
        # if tuple(seq[-4:]) == (-2, 1, -1, 3):
        #     print("S", secret % 10)
        # if tuple(seq[-4:]) == (-2, 2, -1, -1):
        #     print("D", secret % 10)
    # print(seq)
        # print(secret)

        # secret %= (2**24)
    # print(secret)

print(sorted(seqs.items(), key=lambda x: x[1]))

print(answer)
# nie 2528