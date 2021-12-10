# going to create a list the length of the bit commands
# and each entry will be a 2 item list where each is a sum of bit in its position
# the item at [0][0] will be the sum of the first position zeros
# the item at [6][1] will be the sum of the 7th 1's
bit_sum_by_digit = []

list = open('inputs/input_day_3.txt', 'r').read().split('\n')

for index, line in enumerate(list):
    for bit_idx, bit_str in enumerate(line):
        if index == 0:
            bit_sum_by_digit.append([0, 0])
        bit_sum_by_digit[bit_idx][int(bit_str)] += 1
# gamma, most common
# epsilon, least common
epsilon_list = []
gamma_list = []
for pair in bit_sum_by_digit:
    if pair[0] > pair[1]:
        gamma_list.append('0')
        epsilon_list.append('1')
    elif pair[1] > pair[0]:
        gamma_list.append('1')
        epsilon_list.append('0')
    else:
        failure = 'We are equal'

# convert list of str bits into a string and then an integer from a string of bits
gamma_rate = int("".join(gamma_list), 2)
epsilon_rate = int("".join(epsilon_list), 2)

power_consumption = gamma_rate * epsilon_rate

print(f'The gamma, epsilon rates are: {str(gamma_rate)}, {str(epsilon_rate)}')
print(f'The power consumption is {power_consumption}')
print('Done!')

# output looked like
# The gamma, epsilon rates are: 1508, 2587
# The power consumption is 3901196
# Done!
#
# Process finished with exit code 0

