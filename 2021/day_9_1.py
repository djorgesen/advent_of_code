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
                low_points.append({"position":[x,y], "height":point})
    return low_points


if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)
    sample_low_points = determine_low_points(sample_data)
    assert sum([d['height'] + 1 for d in sample_low_points]) == 15

    time_elapsed = time() - start
    print(f'Sample completed in {time_elapsed}')

    start = time()

    challenge_data = get_data(INPUT_PATH)
    challenge_low_points = determine_low_points(challenge_data)
    sum_of_points = sum([d['height'] + 1 for d in challenge_low_points])
    print(f"Part 1: Sum of all low points + 1 is {sum_of_points}.")

    time_elapsed = time() - start
    print(f'Part 1 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
# Part 2: Sum of all outputs is 1020159.
# Part 2 completed in 0.015688657760620117
#
# Process finished with exit code 0