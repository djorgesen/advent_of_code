list = []
with open('inputs/input_day_1_1.txt', 'r') as day_1_file:
    list = day_1_file.read().split('\n')

prior_value = None
increases = 0
decreases = 0
decreased_list = []
for index, item in enumerate(list):
    if (index + 2) >= len(list):
        break
    sum_value = int(list[index]) + int(list[index + 1]) + int(list[index + 2])
    if prior_value is not None and sum_value > prior_value:
        increases += 1
    else:
        decreases += 1
        decreased_list.append({'index': index, 'prior': prior_value, 'value': sum_value})
    prior_value = sum_value
print(f'There were { increases } increases!')
# 1486 was the answer