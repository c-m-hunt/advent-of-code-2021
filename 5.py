import numpy as np


def process_data(lines):
    lines_out = []
    for line in lines:
        parts = line.split("->")
        pt1 = [int(x) for x in parts[0].split(",")]
        pt2 = [int(x) for x in parts[1].split(",")]
        lines_out.append([pt1, pt2])
    return np.array(lines_out)


def get_all_points_between_two_points(pt1, pt2, inc_diag):
    if pt1[0] == pt2[0]:
        max_y = max(pt1[1], pt2[1])
        min_y = min(pt1[1], pt2[1])
        return [[pt1[0], i] for i in range(min_y, max_y + 1)]
    elif pt1[1] == pt2[1]:
        max_x = max(pt1[0], pt2[0])
        min_x = min(pt1[0], pt2[0])
        return [[i, pt1[1]] for i in range(min_x, max_x + 1)]
    else:
        if not inc_diag:
            return []
        points = [pt1.copy(), pt2.copy()]
        while True:
            pt1[0] += 1 if pt1[0] < pt2[0] else -1
            pt1[1] += 1 if pt1[1] < pt2[1] else -1
            points.append(pt1.copy())
            if pt1[0] == pt2[0] and pt1[1] == pt2[1]:
                break
        return list(np.unique(np.array(points), axis=0))


def draw_lines(lines, inc_diag):
    size = np.max(lines) + 1
    grid = np.zeros((size, size))
    for line in lines:
        points = get_all_points_between_two_points(line[0], line[1], inc_diag)
        for pt in points:
            grid[pt[0], pt[1]] += 1
    return grid


filename = "./input/5.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lines = process_data(lines)
grid = draw_lines(lines, False)
count_more_than_2 = sum([1 for x in grid.flatten() if x >= 2])
print("Part 1:", count_more_than_2)

grid = draw_lines(lines, True)
count_more_than_2 = sum([1 for x in grid.flatten() if x >= 2])
print("Part 2:", count_more_than_2)
