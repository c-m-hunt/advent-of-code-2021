filename = "./input/6.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

input_vals = [int(x) for x in lines[0].split(",")]


def spawn_days(fish, days):
    fish_dict = {x: 0 for x in range(8)}
    for v in fish:
        fish_dict[v] += 1
    for d in range(days):
        new_dict = {x: 0 for x in range(9)}
        for i in range(len(fish_dict), 0, -1):
            i = i - 1
            if i == 0:
                new_dict[6] += fish_dict[i]
                new_dict[8] = fish_dict[i]
            else:
                new_dict[i - 1] = fish_dict[i]
        fish_dict = new_dict.copy()
    print(fish_dict)
    return fish_dict


fish = spawn_days(input_vals, 80)
print("Part 1:", sum(fish.values()))

fish = spawn_days(input_vals, 256)
print("Part 2:", sum(fish.values()))
