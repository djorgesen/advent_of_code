from time import time
from copy import copy
from collections import Counter
SAMPLE_PATH = "2021/inputs/input_11.sample.txt"
INPUT_PATH = "2021/inputs/input_11.txt"

ADJACENT_GRID = (
    (-1,-1),
    (0,-1),
    (1,-1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)

class Grid:
    def __init__(self, list_of_values):
        self.grid = list_of_values
        self.flash_counter = {}
        self.step = 0

    def total(self):
        return sum([value for  key, value in self.flash_counter.items()])

    def increment(self):
        self.step += 1
        self.flash_counter[self.step] = 0
        # we know the grid is 100, 10x10
        # loop is 100 each time
        # increment, then flash
        for x in range(10):
            for y in range(10):
                self.grid[x][y] += 1

        # flash loop
        for x in range(10):
            for y in range(10):
                if self.grid[x][y] > 9:
                    self.flash(x,y)

    def increment_x_steps(self, x):
        for _ in range(x):
            self.increment()

    def flash(self, x, y):
        self.grid[x][y] = 0
        self.flash_counter[self.step] += 1
        for additive in ADJACENT_GRID:
            new_x = x + additive[0]
            new_y = y + additive[1]
            if -1 < new_x < 10 and -1 < new_y < 10 and self.grid[new_x][new_y] != 0:
                self.grid[new_x][new_y] += 1
                if self.grid[new_x][new_y] > 9:
                    self.flash(new_x, new_y)

    def increment_until_synchronized(self):
        while self.flash_counter[self.step] != 100:
            self.increment()
            # set a max steps
            if self.step == 300:
                return


def get_data(file_name: str) -> []:
    # file to list of strings
    # to list of  lists of ints
    return [[int(a) for a in c] for c in open(file_name, 'r').read().split('\n')]

if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)
    sample_grid = Grid(sample_data)
    sample_grid.increment_x_steps(10)
    assert sample_grid.total() == 204
    sample_grid.increment_x_steps(90)
    assert sample_grid.total() == 1656
    sample_grid.increment_until_synchronized()
    assert sample_grid.step == 195
    time_elapsed = time() - start
    print(f'Sample completed in {time_elapsed}')

    start = time()

    challenge_data = get_data(INPUT_PATH)
    grid = Grid(challenge_data)
    grid.increment_x_steps(100)
    total_flashes = grid.total()
    print(f"Part 1: {total_flashes} after 100 steps.")
    grid.increment_until_synchronized()
    print(f"Part 2: {grid.step} steps til synchronization.")
    time_elapsed = time() - start
    print(f'Part 1 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
# Sample completed in 2.787877082824707
# Part 1: 1732 after 100 steps.
# Part 2: 290 steps til synchronization.
# Part 1 completed in 38.14857363700867
#
# Process finished with exit code 0