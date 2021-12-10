from time import time
from copy import copy
SAMPLE_PATH = "inputs/input_10.sample.txt"
INPUT_PATH = "inputs/input_10.txt"

CHUNK_DELIMITERS = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}
ERROR_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
COMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

class Command:
    def __init__(self, command_string):
        command = [c for c in command_string]
        success = True
        self.error_char, self.expected_char, self.completion_command = self.find_error(command)
        self.command = command + self.completion_command


    def find_error(self, command):
        opening_brackets = []
        original_command = copy(command)
        error = ''
        expected = ''
        for character in original_command:

            if character in CHUNK_DELIMITERS.keys():
                opening_brackets.append(character)
            elif character == CHUNK_DELIMITERS[opening_brackets[-1][0]]:
                opening_brackets.pop()
            else:
                return character, CHUNK_DELIMITERS[opening_brackets[-1][0]], []
        completion_command = [CHUNK_DELIMITERS[c] for c in opening_brackets]
        return '', '', completion_command




def get_data(file_name: str) -> []:
    return [list(c) for c in  open(file_name, 'r').read().split('\n')]


def calculate_error_score(data):
    score = 0
    completion_scores = []
    for d in data:
        c = Command(d)
        if c.error_char != '':
            score += ERROR_POINTS[c.error_char]
        if len(c.completion_command):
            completion_score = 0
            while len(c.completion_command):
                comm = c.completion_command.pop()
                completion_score = completion_score * 5
                completion_score += COMPLETE_POINTS[comm]
            completion_scores.append(completion_score)
    completion_scores.sort()
    mid_number = int(len(completion_scores)/2)

    return score, completion_scores[mid_number]

if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)
    sample_score, sample_completions = calculate_error_score(sample_data)
    assert sample_score == 26397
    assert sample_completions == 288957
    time_elapsed = time() - start
    print(f'Sample completed in {time_elapsed}')

    start = time()

    challenge_data = get_data(INPUT_PATH)
    challenge_score, challenge_completions = calculate_error_score(challenge_data)
    print(f"Part 1: Error score is {challenge_score}.")
    print(f"Part 2: Completion score is {challenge_completions}.")

    time_elapsed = time() - start
    print(f'Part 1 completed in {time_elapsed}')
total_time_elapsed = time() - full_start

(f'Done in {total_time_elapsed}')

# output
