# going to create a list the length of the bit commands
# and each entry will be a 2 item list where each is a sum of bit in its position
# the item at [0][0] will be the sum of the first position zeros
# the item at [6][1] will be the sum of the 7th 1's
bit_sum_by_digit = []
oxygen_generator_rating = 0
co2_scrubber_rating = 0

list = []
with open('inputs/input_day_3.txt', 'r') as day_1_file:
    list = day_1_file.read().split('\n')


def process_list_for_position(current_list, current_index, digit):
    # each loop we only care about one position
    # and we only care about the least or most
    # least is digit = 0
    # most is digit = 1
    count_of_bits = [0, 0]
    for line in current_list:
        count_of_bits[int(line[current_index])] += 1


    pair = [0, 0]
    if count_of_bits[0] > count_of_bits[1]:
        pair[0] = 1
    elif count_of_bits[1] > count_of_bits[0]:
        pair[1] = 1
    else:
        pair = [digit, digit]

    chosen_bit = pair[digit]
    new_list = []
    # loop through the old list, only grab items that have the bit we want, in the position we care about this iteration
    # if there are more than one, run the function again for the next position
    for line in current_list:
        if int(line[current_index]) == chosen_bit:
            new_list.append(line)

    if len(new_list) == 1:
        return new_list[0]
    else:
        return process_list_for_position(new_list, current_index + 1, digit)

# oxygen generator rating is going to filter on most common ie digit = 1
oxygen_generator_rating = process_list_for_position(list, 0, 1)
# co2 scrubber is least
co2_scrubber_rating = process_list_for_position(list, 0, 0)

# Next, you should verify the
#       life support rating,
# which can be determined by multiplying the
#       oxygen generator rating by the CO2 scrubber rating.

life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


print(f'The oxygen generator, co2 scrubber rates are: {str(oxygen_generator_rating)}, {str(co2_scrubber_rating)}')
print(f'As ints they are: {str(int(oxygen_generator_rating, 2))}, {str(int(co2_scrubber_rating, 2))}')
print(f'The life support rating is {life_support_rating}')
print('Done!')

# output looked like
# The oxygen generator, co2 scrubber rates are: 011001100111, 101010000100
# As ints they are: 1639, 2692
# The life support rating is 4412188
# Done!
#
# Process finished with exit code 0






