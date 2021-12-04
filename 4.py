import numpy as np


def check_row_or_col(card):
    # Rows
    for i in range(5):
        if np.sum(card[i]) == 5:
            return True
    # Columns
    for i in range(5):
        if np.sum(card[j][i] for j in range(5)) == 5:
            return True


def play_bingo(cards, numbers, last_card=False):
    complete_cards = np.zeros(len(cards))
    masks = np.zeros((len(cards), 5, 5), dtype=int)
    for number in numbers:
        for i in range(len(cards)):
            for j in range(5):
                for k in range(5):
                    if cards[i][j][k] == number:
                        masks[i][j][k] = 1

        for i in range(len(cards)):
            if check_row_or_col(masks[i]):
                if not last_card:
                    return cards[i], masks[i], number
                else:
                    complete_cards[i] = 1
                    if np.sum(complete_cards) == len(cards):
                        print(complete_cards)
                        return cards[i], masks[i], number

    return None, None, None


def get_sum(card, mask, marked=1):
    sum = 0
    for i in range(5):
        for j in range(5):
            if mask[i][j] == marked:
                sum += card[i][j]
    return sum


filename = "./input/4.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = []
cards = []
card = []
for i, line in enumerate(lines):
    if i == 0:
        numbers = [int(x) for x in line.split(",")]
        continue

    if line == "":
        if i > 1:
            cards.append(card)
            card = []
        continue

    card.append(np.array([int(line[3 * x : ((3 * x) + 3)]) for x in range(5)]))

cards.append(card)
card, mask, number = play_bingo(cards, numbers)

print(card)
print(mask)
print(number)

sum = get_sum(card, mask)
print("Sum unmarked: ", sum)
print("Winning number: ", sum * number)

card, mask, number = play_bingo(cards, numbers, True)

print(card)
print(mask)
print(number)

sum = get_sum(card, mask, 0)
print("Sum unmarked: ", sum)
print("Winning number: ", sum * number)
