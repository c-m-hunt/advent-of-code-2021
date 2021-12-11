import numpy as np


def step(octs):
    flashes = 0
    flashed = np.zeros(octs.shape)
    octs = octs + np.ones(octs.shape)
    while True:
        finished = True
        for i in range(octs.shape[0]):
            for j in range(octs.shape[1]):
                if octs[i, j] > 9 and flashed[i, j] == 0:
                    finished = False
                    flashed[i, j] = 1
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            if (
                                k >= 0
                                and k < octs.shape[0]
                                and l >= 0
                                and l < octs.shape[1]
                            ):
                                octs[k, l] += 1
        if finished:
            break

    for i in range(octs.shape[0]):
        for j in range(octs.shape[1]):
            if octs[i, j] > 9:
                octs[i, j] = 0
                flashes += 1

    return octs, flashes


filename = "./input/11.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = np.array([[int(n) for n in line.rstrip()] for line in lines], dtype=int)

lines_2 = lines.copy()

all_flashes = 0
for i in range(100):
    lines, flashes = step(lines)
    all_flashes += flashes

print("Final grid: ", lines)
print("Part 1: ", all_flashes)

count = 0
while True:
    count += 1
    lines_2, flashes = step(lines_2)
    if np.sum(lines_2) == 0:
        break
print("Part 2: ", count)
