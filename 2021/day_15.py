from time import time
from collections import deque
from queue import PriorityQueue

from collections import Counter, deque
SAMPLE_PATH = "2021/inputs/input_15.sample.txt"
INPUT_PATH = "2021/inputs/input_15.txt"

def get_data(file_name: str) -> []:
    lines = open(file_name, 'r').read().splitlines()
    return [list(map(int, line)) for line in lines]

def get_lowest_risk(matrix):
    height, width = len(matrix), len(matrix[0])
    pq = PriorityQueue()
    # Add starting position in priority queue
    pq.put((0, (0, 0)))
    visited = {(0, 0), }
    while pq:
        curr_risk, (i, j) = pq.get()
        # Once we reach the end of the matrix, we can stop and return the risk
        if i == height - 1 and j == width - 1:
            return curr_risk
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < height and 0 <= y < width and (x, y) not in visited:
                weight = matrix[x][y]
                pq.put((curr_risk + weight, (x, y)))
                visited.add((x, y))


def expand_matrix(matrix):
    huge_grid = []
    matrix_grid = [[0, 1, 2, 3, 4],
                   [1, 2, 3, 4, 5],
                   [2, 3, 4, 5, 6],
                   [3, 4, 5, 6, 7],
                   [4, 5, 6, 7, 8]
                   ]
    for x in matrix_grid:
        for line in matrix:
            huge_line = []
            for additive in x:
                for risk_value in line:
                    huge_line.append(additive + risk_value if risk_value + additive < 10 else risk_value + additive - 9)
            huge_grid.append(huge_line)
    return huge_grid





if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)
    sample_distance = get_lowest_risk(sample_data)
    assert sample_distance == 40
    sample_big_distance = get_lowest_risk(expand_matrix(sample_data))
    assert sample_big_distance == 315
    time_elapsed = time() - start
    print(f'Sample first ten completed in {time_elapsed}')


    start = time()

    challenge_data = get_data(INPUT_PATH)
    least_risk = get_lowest_risk(challenge_data)

    print(f"Part 1: Least risk route is {least_risk}")
    least_risk_part_2 = get_lowest_risk(expand_matrix(challenge_data))
    print(f"Part 2: Least risk route is {least_risk_part_2}")

    time_elapsed = time() - start
    print(f'Part 1 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
#