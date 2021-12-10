list = []
with open('inputs/input_day_1_1.txt', 'r') as day_1_file:
    list = day_1_file.read().split('\n')

prior_value = None
increases = 0
decreases = 0
decreased_list = []
for index, item in enumerate(list):
    if prior_value is not None and int(item) > prior_value:
        increases += 1
    else:
        decreases += 1
        decreased_list.append({'index': index, 'prior': prior_value, 'value': int(item)})
    prior_value = int(item)
print(f'There were { increases } increases!')
# 1446 was the answer