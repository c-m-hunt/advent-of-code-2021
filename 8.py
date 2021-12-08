filename = "./input/8.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def list_diff(a, b):
    return [item for item in a if item not in b]


def sort_string(string):
    return "".join(sorted(string))


def calculate_numbers(alpha_digits):
    numbers = {}
    segments = ["a", "b", "c", "d", "e", "f", "g"]
    which_seg = {}

    # Find 2
    for a in segments:

        length = len([1 for x in alpha_digits if a in x])
        if length == 6:
            which_seg["b"] = a
        if length == 4:
            which_seg["e"] = a
        if length == 9:
            which_seg["f"] = a
            for x in alpha_digits:
                if a not in x:
                    numbers[2] = x
        if length == 8:
            which_seg["g"] = a

    count = 0
    while True:
        count += 1
        if count == 50:
            break
        for alpha in alpha_digits:
            if len(alpha) == 2:
                numbers[1] = alpha
            if len(alpha) == 3:
                numbers[7] = alpha
                if 1 in numbers.keys():
                    which_seg["a"] = list_diff(numbers[7], numbers[1])[0]
            if len(alpha) == 4:
                numbers[4] = alpha
            if len(alpha) == 7:
                numbers[8] = alpha
            if len(alpha) == 5:
                if (
                    5 in numbers.keys()
                    and 2 in numbers.keys()
                    and alpha != numbers[5]
                    and alpha != numbers[2]
                ):
                    numbers[3] = alpha
                if which_seg["b"] in alpha:
                    numbers[5] = alpha
            if len(alpha) == 6:
                if 3 in numbers.keys() and alpha != numbers[3]:
                    if len(list_diff(alpha, numbers[3])) == 1:
                        numbers[9] = alpha
                if 9 in numbers.keys() and alpha != numbers[9]:
                    if len(list_diff(alpha, numbers[5])) == 1:
                        numbers[6] = alpha
                    else:
                        numbers[0] = alpha
                pass

    numbers_out = {}
    for n in numbers.keys():
        numbers_out[sort_string(numbers[n])] = n
    return numbers_out


sizes = {}
for line in lines:
    for n in line.split("|")[1].split(" "):
        sizes[len(n)] = sizes.get(len(n), 0) + 1

print("Part 1:", sizes[2] + sizes[4] + sizes[3] + sizes[7])

# Part 2
total = 0
for lines in lines:
    input_list = [x for x in lines.split("|")[0].split(" ") if x != ""]
    numbers = calculate_numbers(input_list)
    number = [
        numbers[sort_string(n)] for n in lines.split("|")[1].split(" ") if n != ""
    ]
    total += int("".join([str(x) for x in number]))

print("Part 2:", total)
