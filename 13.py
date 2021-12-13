import numpy as np


def do_fold(grid, fold):
    axis = 1 if fold[0] == "x" else 0
    line = fold[1]

    fold_bit = grid[line + 1 :] if axis == 0 else grid[:, line + 1 :]
    fold_bit = np.flip(fold_bit, axis=axis)

    if axis == 0:
        grid_out = grid[0 : fold_bit.shape[0]] + fold_bit
    else:
        grid_out = grid[:, 0 : fold_bit.shape[1]] + fold_bit

    return grid_out


filename = "./input/13.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

dots = []
folds = []

doing_dots = True
for line in lines:
    if line == "":
        doing_dots = False
    else:
        if doing_dots:
            dots.append([int(x) for x in line.split(",")])
        else:
            folds.append([line.split("=")[0].split(" ")[-1], int(line.split("=")[1])])


max_x = max([x[0] for x in dots])
max_y = max([x[1] for x in dots])

grid = np.zeros((max_y + 1, max_x + 1))

for dot in dots:
    grid[dot[1]][dot[0]] = 1

grid = do_fold(grid, folds[0])

print("Part 1: ", sum([1 for x in grid.flatten() if x >= 1]))

for fold in folds[1:]:
    grid = do_fold(grid, fold)

print("Part 2: ")

for row in grid:
    print("".join(["*" if x >= 1 else " " for x in row]))
