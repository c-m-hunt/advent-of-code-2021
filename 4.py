import numpy as np


def check_row_or_col(card):
    # Rows
    complete_rows = np.any(np.equal(5, (np.sum(card, axis=1))))
    if complete_rows:
        return True
    # Columns
    complete_columns = np.any(np.equal(5, (np.sum(card, axis=0))))
    return complete_columns


def play_bingo(cards, numbers, last_card=False):
    complete_cards = np.zeros(len(cards))
    masks = np.zeros((len(cards), 5, 5), dtype=bool)
    for number in numbers:
        masks += np.equal(number, cards)

        for i in range(len(cards)):
            if check_row_or_col(masks[i]):
                if not last_card:
                    return cards[i], masks[i], number
                else:
                    complete_cards[i] = 1
                    if np.sum(complete_cards) == len(cards):
                        return cards[i], masks[i], number

    return None, None, None


def get_sum(card, mask):
    return np.sum(card * np.invert(mask))


def generate_cards(lines):
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
    return numbers, cards


filename = "./input/4.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers, cards = generate_cards(lines)

card, mask, number = play_bingo(cards, numbers)

print(
    """
##########
PART 1
##########
"""
)

print(card)
print(mask)
print(number)

sum = get_sum(card, mask)
print("Sum unmarked: ", sum)
print("Winning number: ", sum * number)

card, mask, number = play_bingo(cards, numbers, True)

print(
    """
##########
PART 2
##########
"""
)

print(card)
print(mask)
print(number)

sum = get_sum(card, mask)
print("Sum unmarked: ", sum)
print("Winning number: ", sum * number)
