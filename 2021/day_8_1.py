from time import time
from collections import deque, Counter
SAMPLE_PATH = "inputs/input_8.sample.txt"
INPUT_PATH = "inputs/input_8.txt"
DIGITS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

class UniquePattern:
    def __init__(self, pattern):
        self.pattern = pattern

    def __len__(self):
        return len(self.pattern)

class Entry:
    patterns = []
    output = []
    def __init__(self, patterns: [str], output: [str] ):
        self.patterns = [UniquePattern(pat) for pat in patterns]
        self.output = [UniquePattern(out) for out in output]



def get_data(file_name: str) -> []:
    lines = open(file_name, 'r').read().split('\n')
    entries = []
    for line in lines:
        parts = line.split('|')
        unique_patterns = parts[0].split()
        output = parts[1].split()
        entry = Entry(unique_patterns,output)
        entries.append(entry)
    return entries



def count_easy_digits(entries):
    counter = Counter()
    for entry in entries:
        counter = counter + Counter([len(digit) for digit in entry.output])
    # we only care about unique char lengths, this is the length of
    # 1: len(DIGITS[1]) == 2
    # 4: len(DIGITS[4]) == 4
    # 7: len(DIGITS[7]) == 3
    # 8: len(DIGITS[8]) == 7

    return sum([counter[len(DIGITS[d])] for d in [1,4,7,8] ])




if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)
    assert count_easy_digits(sample_data) == 26

    challenge_data = get_data(INPUT_PATH)
    digit_count = count_easy_digits(challenge_data)
    print(f"1, 4, 7, 8 appear {digit_count} times.")
    time_elapsed = time() - start
    print(f'Part 1 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
# Sample minimum moves is 37.
# Sample completed in 0.35119056701660156
# Part 1 minimum moves is 349769.
# Part 1 completed in 436.1567497253418
# Done in 436.17725372314453
#
# Process finished with exit code 0
