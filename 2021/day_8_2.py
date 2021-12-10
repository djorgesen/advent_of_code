from time import time
from collections import deque, Counter
from copy import copy
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
POSSIBLE_SEGMENTS = set([char for char in 'abcdefg'])
SEGMENT_MAP = {
    'a': copy(POSSIBLE_SEGMENTS),
    'b': copy(POSSIBLE_SEGMENTS),
    'c': copy(POSSIBLE_SEGMENTS),
    'd': copy(POSSIBLE_SEGMENTS),
    'e': copy(POSSIBLE_SEGMENTS),
    'f': copy(POSSIBLE_SEGMENTS),
    'g': copy(POSSIBLE_SEGMENTS)
}

class UniquePattern:
    def __init__(self, pattern):
        self.pattern = set([c for c in pattern])
        possible_digits = copy(DIGITS)
        self.possible_digits = {}
        for dig, pat in possible_digits.items():
            if len(pat) == len(pattern):
                self.possible_digits[dig] = pat
        self.digit = None
        if len(self.possible_digits) == 1:
            for digit in self.possible_digits.keys():
                self.digit = digit

    def __len__(self):
        return len(self.pattern)
    def __repr__(self):
        return self.digit if self.digit is not None else ''
    def __str__(self):
        return str(self.digit) if self.digit is None else ''

class Entry:

    def __init__(self, patterns: [str], output: [str] ):
        self.patterns = []
        mapped_patterns = [None] * 10
        self.output = []
        self.segment_map = copy(SEGMENT_MAP)
        unknowns_exist = False

        for pat in patterns:
            up = UniquePattern(pat)
            if up.digit is not None:
                mapped_patterns[up.digit] = up
                self.reduce_segments(up.digit, up.pattern)
            self.patterns.append(up)

        for item in output:
            item_set = set([c for c in item])
            for pat in self.patterns:
                if pat.pattern == item_set:
                    self.output.append(pat)
                if pat.digit is None:
                    unknowns_exist = True

        # on the off chance that we just know all the outputs already, don't bother with anything else
        if not unknowns_exist:
            return

        # of the 5 length patterns, the one that contains 7 is 3
        # of the 6 length patterns, the one that does not contain 7 is 6
        for i in self.patterns:
            if i.digit is not None:
                continue
            if len(i) == 5 and i.pattern.issuperset(mapped_patterns[7].pattern):
                i.digit = 3
                mapped_patterns[3] = i
            if len(i) == 6 and not i.pattern.issuperset(mapped_patterns[7].pattern):
                i.digit = 6
                mapped_patterns[6] = i
        # now the 6 that contains 3 is 9, the other is 0
        for i in self.patterns:
            if i.digit is not None:
                continue
            if len(i) == 6 and i.pattern.issuperset(mapped_patterns[3].pattern):
                i.digit = 9
                mapped_patterns[9] = i
            if len(i) == 6 and not i.pattern.issuperset(mapped_patterns[3].pattern):
                i.digit = 0
                mapped_patterns[0] = i
        # of the 5 digit ones, the difference between 8 and 9 is in 2 but not 5
        subset = mapped_patterns[8].pattern - mapped_patterns[9].pattern
        for i in self.patterns:
            if i.digit is not None:
                continue
            if len(i) == 5 and i.pattern.issuperset(subset):
                i.digit = 2
                mapped_patterns[2] = i
            if len(i) == 5 and not i.pattern.issuperset(subset):
                i.digit = 5
                mapped_patterns[5] = i
        self.mapped_patterns = mapped_patterns


    def map_segments(self):
        pass

    def reduce_segments(self, digit, pattern):
        # if a character is in the default digit segment map
        # then it must be limited to characters in this pattern
        for char in DIGITS[digit]:
            self.segment_map[char] = self.segment_map[char].intersection(pattern)

        # the segments that aren't involved in this digit
        # also have to remove the characters in this pattern
        for char in POSSIBLE_SEGMENTS:
            if char not in DIGITS[digit]:
                self.segment_map[char] = self.segment_map[char] - pattern

        # all the maps will be 1 or 2 digits
        # and each of the 2s will have a matching segment
        # find a digit that just has one of them
        # for char, mapping in self.segment_map.items:
        #     if len(mapping) == 2:
        #

    @property
    def decoded_pattern(self):
        return int("".join([str(out.digit) for out in self.output]))

    def __repr__(self):
        return self.decoded_pattern()


def get_data(file_name: str = None, alt_str: str = '') -> []:
    if file_name:
        lines = open(file_name, 'r').read().split('\n')
    else:
        lines = [alt_str]
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
    assert sum([s.decoded_pattern for s in sample_data]) == 61229
    challenge_data = get_data(INPUT_PATH)
    sum_of_outputs =  sum([s.decoded_pattern for s in challenge_data])

    print(f"Part 2: Sum of all outputs is {sum_of_outputs}.")

    time_elapsed = time() - start
    print(f'Part 2 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
# Part 2: Sum of all outputs is 1020159.
# Part 2 completed in 0.015688657760620117
#
# Process finished with exit code 0