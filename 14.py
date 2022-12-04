from collections import Counter

filename = "./input/14.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

temp = [c for c in lines[0]]
trans = {}

doing_dots = True
for line in lines[2:]:
    parts = line.split("->")
    trans[parts[0].strip()] = parts[1].strip()


def step(input, trans):
    output = ""
    for i in range(len(input) - 1):
        pair = "".join(input[i : i + 2])
        if pair in trans:
            output += input[i] + trans[pair]
        else:
            print(i)
            output += input[i]
    output += input[-1]
    return output


def count_n_step(input, trans, n=10):
    for j in range(10):
        input = step(input, trans)
    c = Counter([c for c in input])
    return input, c


out, c = count_n_step(temp, trans)
print(out)

min_val = min(c.values())
max_val = max(c.values())

print("Part 1: ", max_val - min_val)

ten_step_output = {}
ten_step_count = {}
for key in trans.keys():
    out, count = count_n_step(key, trans)
    ten_step_count[key] = count
    ten_step_output[key] = out


for i in range(4):
    pass


# for j in range(10, 20):
#     temp = step(temp, trans)

# c = Counter([c for c in temp])
# min_val = min(c.values())
# max_val = max(c.values())

# print("Part 2: ", max_val - min_val)
