matches = {"(": ")", "[": "]", "{": "}", "<": ">"}


def validate_input(input):
    stack = []
    for char in input:
        if char in matches.keys():
            stack.append(matches[char])
        elif char == stack[-1]:
            stack.pop()
        else:
            return False, char, stack
    return True, None, stack


filename = "./input/10.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [[n for n in line.rstrip()] for line in lines]

points2 = {")": 1, "}": 3, "]": 2, ">": 4}


def calculate_stack_score(stack):
    stack_total = 0
    for c in stack:
        stack_total *= 5
        stack_total += points2[c]
    return stack_total


points = {")": 3, "}": 1197, "]": 57, ">": 25137}

total1 = 0
total2 = []
for line in lines:
    valid, char, stack = validate_input(line)
    if not valid:
        total1 += points[char]
    else:
        stack_total = 0
        stack.reverse()
        stack_total = calculate_stack_score(stack)
        total2.append(stack_total)
total2.sort()
print(total2)
print("Part 2:", total2[(len(total2) // 2)])
