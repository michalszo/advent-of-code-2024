from collections.abc import Sequence
from os.path import exists
from example_input import get_example_input

ii = lambda _i: int(_i) if _i.isnumeric() else _i

def is_sequence(obj):
    return isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray))

def parse_data(obj, *args):
    if len(args) == 1:
        return obj.split(args[0])
    else:
        return [parse_data(i, args[1:]) for i in obj.split(args[0])]


def load_data(day, year=2024):
    if not exists(f"{day}.txt") or open(f"{day}.txt").read().strip() == '':
        print("Loading data...")
        import requests
        data = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session":open("session_id.txt").read()}).text.strip()
        if not data.startswith("Please don't"):
            open(f"{day}.txt", "w").write(data)
            return data
    else:
        return open(f"{day}.txt").read().strip()

def load_test_data(day, year=2024):
    if not exists(f"{day}_test.txt") or open(f"{day}_test.txt").read().strip() == '':
        print("Loading test data...")
        data = get_example_input(day, year)
        if not data:
            return False
        if not data.startswith("Please don't"):
            open(f"{day}_test.txt", "w").write(data)
            return data
    else:
        return open(f"{day}_test.txt").read().strip()