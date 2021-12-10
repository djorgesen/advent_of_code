from time import time
SAMPLE_PATH = "inputs/input_9.sample.txt"
INPUT_PATH = "inputs/input_9.txt"

def get_data(file_name: str) -> []:
    if file_name:
        lines = open(file_name, 'r').read().split('\n')
    cave_map = []
    for line in lines:
        cave_map.append([int(c) for c in line])
    return cave_map

class Basin:
    def __init__(self, cave_map, low_position):
        self.cave_map = cave_map
        self.low_position = low_position
        self.basin = {(low_position[0],low_position[1])}
        self.find_adjacent_basin_positions(low_position)

    def find_adjacent_basin_positions(self, position):
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        for direction in directions:
            new_position = (position[0]+direction[0],position[1]+direction[1])
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] == len(self.cave_map) or new_position[1] == len(self.cave_map[0]):
                continue
            if new_position not in self.basin and self.cave_map[new_position[0]][new_position[1]] != 9:
                self.basin.add(new_position)
                self.find_adjacent_basin_positions(new_position)


def determine_low_points(cave_map: [[int]]) -> [{}]:
    # get dimensions of map
    length = len(cave_map)
    width = len(cave_map[0])

    low_points = []
    # determine if a point is lower than the numbers around it
    for x in range(length):
        for y in range(width):
            point = cave_map[x][y]
            w_point, n_point, e_point, s_point = None, None, None, None
            if x != 0:
                w_point = cave_map[x - 1][y]
            if y != 0:
                n_point = cave_map[x][y - 1]
            if x + 1 != length:
                e_point = cave_map[x + 1][y]
            if y + 1 != width:
                s_point = cave_map[x][y + 1]

            if (w_point is None or w_point > point) and (e_point is None or e_point > point) and (s_point is None or s_point > point) and (n_point is None or n_point > point):
                basin = Basin(cave_map, (x,y))
                low_points.append({"position":(x,y), "height":point, "basin": basin})
    return low_points

def sort_by_basin_size(a):
    return len(a.get('basin').basin)

if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)
    sample_low_points = determine_low_points(sample_data)
    assert sum([d['height'] + 1 for d in sample_low_points]) == 15
    assert len(sample_low_points[0]['basin'].basin) == 3
    assert len(sample_low_points[1]['basin'].basin) == 9
    assert len(sample_low_points[2]['basin'].basin) == 14
    assert len(sample_low_points[3]['basin'].basin) == 9
    sample_low_points.sort(key=sort_by_basin_size, reverse=True)
    sample_product_of_basin_sizes = len(sample_low_points[0]['basin'].basin) * len(sample_low_points[1]['basin'].basin) * len(sample_low_points[2]['basin'].basin)
    assert sample_product_of_basin_sizes == 1134
    time_elapsed = time() - start
    print(f'Sample completed in {time_elapsed}')

    start = time()

    challenge_data = get_data(INPUT_PATH)
    challenge_low_points = determine_low_points(challenge_data)
    sum_of_points = sum([d['height'] + 1 for d in challenge_low_points])
    assert sum_of_points == 558
    print(f"Part 1: Sum of all low points + 1 is {sum_of_points}.")
    challenge_low_points.sort(key=sort_by_basin_size, reverse=True)
    product_of_basin_sizes = len(challenge_low_points[0]['basin'].basin) * len(
        challenge_low_points[1]['basin'].basin) * len(challenge_low_points[2]['basin'].basin)
    print(f'Product of the 3 largest basin Sizes is {product_of_basin_sizes}.')
    time_elapsed = time() - start
    print(f'Part 2 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
# Part 2: Sum of all outputs is 1020159.
# Part 2 completed in 0.015688657760620117
#
# Process finished with exit code 0