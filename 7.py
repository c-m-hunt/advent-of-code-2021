def get_cost_to_move_part1(crabs, pos):
    return sum([abs(crabs[i] - pos) for i in range(len(crabs))])


def get_cost_to_move_part2(crabs, pos, dist_moved):
    return sum([dist_moved[abs(crabs[i] - pos)] for i in range(len(crabs))])


filename = "./input/7.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

crabs = [int(x) for x in lines[0].split(",")]
max_pos = max(crabs)

costs = [get_cost_to_move_part1(crabs, i) for i in range(max_pos)]
index_min = min(range(len(costs)), key=costs.__getitem__)
print("Part 1:", min(costs), index_min)

dist_moved = {dist: sum(range(1, dist + 1)) for dist in range(max(crabs) + 1)}
costs = [get_cost_to_move_part2(crabs, i, dist_moved) for i in range(max_pos)]
index_min = min(range(len(costs)), key=costs.__getitem__)
print("Part 2:", min(costs), index_min)
