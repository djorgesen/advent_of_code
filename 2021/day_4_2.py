def check_card(card, bingo_numbers):
    sum_uncalled = 0
    is_match = False
    bingo_set = set(bingo_numbers)
    card_set = set().union(*[frozenset(line) for line in card])
#   check each row
#   if there are less than 5 intersections then no point in looking further.
    if len(bingo_set.intersection(card_set)) < 5:
        return False, 0

    for row in card:
        if set(row).issubset(bingo_set):
            is_match = True
            break
    if not is_match:
        for card_index in range(5):
            vertical_set = set([card[0][card_index], card[1][card_index], card[2][card_index], card[3][card_index],
                                card[4][card_index]])
            if vertical_set.issubset(bingo_set):
                is_match = True
                break
    # if not is_match:
    #     diagonal_top_set = set([card[0][0], card[1][1], card[2][2], card[3][3], card[4][4]])
    #     if diagonal_top_set.issubset(bingo_set):
    #         is_match = True
    # if not is_match:
    #     diagonal_bottom_set = set([card[4][0], card[3][1], card[2][2], card[1][3], card[0][4]])
    #     if diagonal_bottom_set.issubset(bingo_set):
    #         is_match = True
    if is_match:
        for i in range(5):
            for j in range(5):
                if not card[i][j]in bingo_set:
                    sum_uncalled += int(card[i][j])
    return is_match, sum_uncalled


list =  open('inputs/input_4.txt', 'r').read().split('\n')

numbers_called = list.pop(0).split(',')
list.pop(0)
cards = []
for index in range(int(len(list)/6) + 1):
    new_card = []
    for i in range(5):
        new_card.append(list[index*6 + i].split())
    cards.append(new_card)


is_match = False
card_sum = 0
last_number = 0
product = 0


for i in range(len(cards) - 4):
    matches_this_loop = 0
    for card_index, card in enumerate(cards):
        current_numbers = numbers_called[:i+5]
        is_match, card_sum = check_card(card, current_numbers)
        if is_match:
            cards.pop(card_index)
            last_number = int(current_numbers[-1])
            product = card_sum * last_number
            matches_this_loop += 1
    if matches_this_loop > 0:
        print(f'Loop {i} has {matches_this_loop} matches.')
    if matches_this_loop == 100:
        break


print(f'Found a match on card {card_index}.')
print(f'The sum of unmatched numbers is {card_sum}')
print(f'The last number was {last_number}')
print(f'and the product is {product}')


print('Done!')

# output looked like
#Loop 24 has 1 matches.
# Loop 31 has 2 matches.
# Loop 35 has 2 matches.
# Loop 36 has 3 matches.
# Loop 37 has 2 matches.
# Loop 38 has 3 matches.
# Loop 39 has 3 matches.
# Loop 40 has 4 matches.
# Loop 41 has 2 matches.
# Loop 42 has 1 matches.
# Loop 44 has 1 matches.
# Loop 45 has 1 matches.
# Loop 46 has 1 matches.
# Loop 47 has 1 matches.
# Loop 48 has 5 matches.
# Loop 49 has 2 matches.
# Loop 50 has 6 matches.
# Loop 52 has 4 matches.
# Loop 53 has 1 matches.
# Loop 54 has 3 matches.
# Loop 55 has 4 matches.
# Loop 56 has 1 matches.
# Loop 57 has 2 matches.
# Loop 58 has 3 matches.
# Loop 59 has 4 matches.
# Loop 60 has 2 matches.
# Loop 61 has 3 matches.
# Loop 62 has 2 matches.
# Loop 63 has 5 matches.
# Loop 64 has 5 matches.
# Loop 65 has 1 matches.
# Loop 66 has 2 matches.
# Loop 67 has 2 matches.
# Loop 68 has 5 matches.
# Loop 69 has 2 matches.
# Loop 70 has 3 matches.
# Loop 71 has 1 matches.
# Loop 72 has 1 matches.
# Loop 73 has 1 matches.
# Loop 74 has 1 matches.
# Loop 75 has 1 matches.
# Loop 78 has 1 matches.
# Found a match on card 0.
# The sum of unmatched numbers is 195
# The last number was 14
# and the product is 2730
# Done!
#
# Process finished with exit code 0






