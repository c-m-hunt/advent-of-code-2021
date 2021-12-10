import numpy as np


def find_low_points(map):
    low_points = []
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            no = map[i, j]
            if (
                (i == 0 or no < map[i - 1, j])
                and (i == map.shape[0] - 1 or no < map[i + 1, j])
                and (j == 0 or no < map[i, j - 1])
                and (j == map.shape[1] - 1 or no < map[i, j + 1])
            ):
                low_points.append([i, j])
    return low_points


def find_basin(map, point):
    basin = np.zeros(map.shape)
    basin[point[0], point[1]] = 1
    checked = []

    def find_neighbours(point):
        neighbors = []
        for [i, j] in [
            [point[0] - 1, point[1]],
            [point[0] + 1, point[1]],
            [point[0], point[1] - 1],
            [point[0], point[1] + 1],
        ]:
            if (
                [i, j] != point
                and i >= 0
                and i < map.shape[0]
                and j >= 0
                and j < map.shape[1]
            ):
                neighbors.append([i, j])
        return neighbors

    def check_point(point):
        for i in find_neighbours(point):
            if map[i[0], i[1]] < 9 and i not in checked:
                basin[i[0], i[1]] = 1
                checked.append(i)
                check_point(i)

    check_point(point)
    return basin


filename = "./input/9.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [[int(n) for n in line.rstrip()] for line in lines]

input_arr = np.array(lines)
low_points = find_low_points(input_arr)
print(low_points)
print("Part 1: ", sum([input_arr[pt[0], pt[1]] for pt in low_points]) + len(low_points))

basins = [find_basin(input_arr, p) for p in low_points]
basin_sizes = [np.sum(basin) for basin in basins]
basin_sizes.sort()
print("Part 2: ", np.prod(basin_sizes[-3:]))
