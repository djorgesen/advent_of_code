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
    if is_match:
        break
    for card_index, card in enumerate(cards):
        current_numbers = numbers_called[:i+5]
        is_match, card_sum = check_card(card, current_numbers)
        if is_match:
            last_number = int(current_numbers[-1])
            product = card_sum * last_number
            break
    if not is_match:
        print(f'No matches in loop {i}')



print(f'Found a match on card {card_index}.')
print(f'The sum of unmatched numbers is {card_sum}')
print(f'The last number was {last_number}')
print(f'and the product is {product}')


print('Done!')

# output looked like
# The oxygen generator, co2 scrubber rates are: 011001100111, 101010000100
# As ints they are: 1639, 2692
# The life support rating is 4412188
# Done!
#
# Process finished with exit code 0






