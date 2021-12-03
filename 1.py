from typing import List


def number_of_increases(nos: List[int]) -> int:
    inc = 0
    prev = None
    for i in nos:
        if prev is not None:
            if i > prev:
                inc += 1
        prev = i
    return inc


def number_of_increases_with_windows(nos: List[int]) -> int:
    inc = 0
    for i in range(len(nos) - 2):
        print(sum(nos[i : i + 3]))
        if sum(nos[i : i + 3]) < sum(nos[i + 1 : i + 4]):
            inc += 1
    return inc


filename = "./input/1.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

increases = number_of_increases(lines)
print(f"Number of increases: {increases}")

increase_windows = number_of_increases_with_windows(lines)
print(f"Number of increases with windows: {increase_windows}")
