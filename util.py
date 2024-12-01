from collections.abc import Sequence
from os.path import exists
from example_input import get_example_input

ii = lambda _i: int(_i) if _i.isnumeric() else _i

def is_sequence(obj):
    return isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray))

def find_neighbors(table, position, offests):
    shape = (len(table[0]), len(table))
    return [table[position[1]+y][position[0]+x] for x, y in offests if 0 <= position[1]+y < shape[1] and 0 <= position[0]+y < shape[0]]

def find_neighbors_3d(table, position, offests):
    shape = (len(table[0][0]), len(table[0]), len(table))
    return [table[position[2]+z][position[1]+y][position[0]+x] for x, y, z in offests if 0 <= position[2]+y < shape[2] and 0 <= position[1]+y < shape[1] and 0 <= position[0]+y < shape[0]]

def shortest_path(start, end, connections):
    current = [[start]]
    new = []
    while 1:
        for path in current:
            for node in connections[path[-1]]:
                if node not in path:
                    new.append(path+[node])
                if node == end:
                    return path[1:]+[node]
        current = new.copy()

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