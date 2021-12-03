
def get_depth_and_dist(commands):
    depth = 0
    dist = 0
    for command in commands:
        if command[0] == 'forward':
            dist += int(command[1])
        if command[0] == 'back':
            dist -= int(command[1])
        if command[0] == 'up':
            depth -= int(command[1])
        if command[0] == 'down':
            depth += int(command[1])
    return depth, dist

def get_depth_and_dist_with_aim(commands):
    depth = 0
    dist = 0
    aim = 0
    for command in commands:
        if command[0] == 'forward':
            dist += int(command[1])
            depth += aim * int(command[1])
        if command[0] == 'up':
            aim -= int(command[1])
        if command[0] == 'down':
            aim += int(command[1])
    return depth, dist

filename = "./input/2.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip().split(" ") for line in lines]

depth, dist = get_depth_and_dist_with_aim(lines)

print(depth * dist)