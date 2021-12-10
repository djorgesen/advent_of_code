from time import time
from collections import deque, Counter
class CrabSwarm:
    def __init__(self, list_of_crab_positions):
        highest_position = max(list_of_crab_positions)
        # positions is a count of crabs in each position
        self.positions = deque(Counter(list_of_crab_positions)[i] for i in range(highest_position + 1))
        # how much fuel it would take to get each crab to a position
        self.moves_per_position = deque()
        for i in range(highest_position):
            moves = 0
            for position, count_of_crabs  in enumerate(self.positions):
                # don't care about counts of 0 or crabs that don't have to move
                if count_of_crabs == 0 or position - i == 0:
                    continue
                distance = abs(position - i)
                # fuel used costs 1 more each unit moved is 1  per distance
                fuel_used_per_crab = (distance^2 + distance) / 2
                moves += fuel_used_per_crab * count_of_crabs
            self.moves_per_position.append(moves)

def act_on_file(file_name):


    list_of_positions = open(file_name, 'r').read().split('\n')[0].split(',')
    crab_list = [int(c) for c in list_of_positions]
    swarm = CrabSwarm(crab_list)
    fewest_moves = min(swarm.moves_per_position)

    return fewest_moves



full_start = time()
start = time()
sample_moves = act_on_file('inputs/input_7.sample.txt')
time_elapsed = (time() - start) * 1000

print(f'Sample minimum moves is {sample_moves}.')
print(f'Sample completed in {time_elapsed}')

full_start = time()
start = time()
part_1_moves = act_on_file('inputs/input_7.txt')
time_elapsed = (time() - start) * 1000

print(f'Part 1 minimum moves is {part_1_moves}.')
print(f'Part 1 completed in {time_elapsed}')


total_time_elapsed = (time() - full_start) * 1000
print(f'Done in {total_time_elapsed}')

# output
# Sample minimum moves is 37.
# Sample completed in 0.35119056701660156
# Part 1 minimum moves is 349769.
# Part 1 completed in 436.1567497253418
# Done in 436.17725372314453
#
# Process finished with exit code 0
