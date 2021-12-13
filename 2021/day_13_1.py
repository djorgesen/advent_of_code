from time import time
from copy import copy
SAMPLE_PATH = "2021/inputs/input_13.sample.txt"
INPUT_PATH = "2021/inputs/input_13.txt"

def get_data(file_name: str) -> []:
    lines = open(file_name, 'r').read().split('\n')
    dots = set()
    commands = []
    max_x = 0
    max_y = 0
    commands_started = False
    for line in lines:
        if line == '':
            commands_started = True
            continue
        if commands_started:
            commands.append(line)
        else:
            dot = line.split(',')
            x = int(dot[0])
            y = int(dot[1])
            dots.add((x, y))
            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y
    return {"size": [max_x + 1, max_y + 1], "dots": dots, "commands": commands}

def fold_paper(paper: dict):
    command = paper.get('commands').pop(0)
    commands = command.split('=')
    line_dimension = 0 #x is typically the 0 position
    new_points = set()
    if commands[0] == 'fold along y':
        line_dimension = 1 # 1 is typically y
    fold_line = int(commands[1])
    for dot in paper.get('dots'):
        if dot[line_dimension] > fold_line:
            new_dot_pos = fold_line - (dot[line_dimension] - fold_line)
            if line_dimension == 0:
                new_points.add((new_dot_pos, dot[1]))
            else:
                new_points.add((dot[0], new_dot_pos))
        else:
            new_points.add(dot)
    paper['dots'] = new_points
    paper.get('size')[line_dimension] =  fold_line
    return paper


def print_grid(data):
    size = data.get('size')
    grid = [["."] * size[0] for _ in range(size[1])]
    for dot in data.get('dots'):
        # reverse the x y since printing 1 row at a time
        grid[dot[1]][dot[0]] = "#"

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)

    sample_data = fold_paper(sample_data)
    assert len(sample_data.get('dots')) == 17
    while len(sample_data.get('commands')) > 0:
        sample_data = fold_paper(sample_data)
    print_grid(sample_data)
    # check that this prints
    # #####
    # #...#
    # #...#
    # #...#
    # #####
    # .....
    # .....
    time_elapsed = time() - start
    print(f'Sample completed in {time_elapsed}')

    start = time()

    challenge_data = get_data(INPUT_PATH)
    challenge_data = fold_paper(challenge_data)
    print(f"Part 1: {len(challenge_data.get('dots'))} dots visible after 1 fold.")
    while len(challenge_data.get('commands')) > 0:
        sample_data = fold_paper(challenge_data)
    print_grid(challenge_data)
    time_elapsed = time() - start
    print(f'Part 1 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
# #####
# #...#
# #...#
# #...#
# #####
# .....
# .....
# Sample completed in 0.0003070831298828125
# Part 1: 653 dots visible after 1 fold.
# #....#..#.###..####.###..###..###..#..#.
# #....#.#..#..#.#....#..#.#..#.#..#.#.#..
# #....##...#..#.###..###..#..#.#..#.##...
# #....#.#..###..#....#..#.###..###..#.#..
# #....#.#..#.#..#....#..#.#....#.#..#.#..
# ####.#..#.#..#.####.###..#....#..#.#..#.
# Part 1 completed in 0.0017430782318115234
#
# Process finished with exit code 0
# Part 2 answer is LKREBPRK