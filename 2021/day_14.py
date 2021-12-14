from time import time
from copy import copy
from collections import Counter, deque
SAMPLE_PATH = "2021/inputs/input_14.sample.txt"
INPUT_PATH = "2021/inputs/input_14.txt"

def get_data(file_name: str) -> []:
    lines = open(file_name, 'r').read().split('\n')
    template = lines.pop(0)
    empty = lines.pop(0)
    rules = {}
    for line in lines:
        rule = line.split(' -> ')
        rules[rule[0]] = rule[1]

    return {"template": template, "rules": rules}

def original_insert_pair(data):
    template = data.get('template')
    rules = data.get('rules')
    new_pairs = []
    for i in range(len(template) - 1):
        pair = "".join([template[i], template[i+1]])
        if i == 0:
            new_pair = [template[i], rules[pair], template[i+1]]
        else:
            new_pair = [rules[pair], template[i + 1]]

        new_pairs += new_pair
    data['template'] = new_pairs
    print('inserted a pair')
    return data

# deque version, not much faster
def deque_insert_pair(data):
    template = deque(data.get('template'))
    rules = data.get('rules')
    new_pairs = deque()
    while template:
        a = template.popleft()
        new_pairs.append(a)
        if template:
            new_pairs.append(rules[a + template[0]])

    data['template'] = new_pairs
    print('inserted a pair')
    return data

def build_bigrams(template):
  p = '^'+ template
  return Counter(p[i:i+2] for i in range(len(p)-1))

def insert_pair(data):
    bigrams = data.get('bigrams')
    expanded_bigrams = Counter()
    rules = data.get('rules')
    for bigram, count in bigrams.items():
        if bigram not in rules:
            expanded_bigrams[bigram] += count
        else:
            rule = rules[bigram]
            expanded_bigrams[bigram[0] + rule] += count
            expanded_bigrams[rule + bigram[1]] += count
    data['bigrams'] = expanded_bigrams
    return data

def insert_x_pairs(data: dict, x: int) -> dict:
    for _ in range(x):
        data = insert_pair(data)
    return data



def count_template(bigrams):
    # template_list = [a for a in template]
    # return Counter(template_list)
    # count only the second element of a pair, first should have been counted already or is dummy
    counts = Counter()
    for (_, x), c in bigrams.items():
        counts[x] += c
    return counts


if __name__ == "__main__":
    full_start = time()
    start = time()

    sample_data = get_data(SAMPLE_PATH)
    sample_data['bigrams'] = build_bigrams(sample_data.get('template'))
    sample_data = insert_x_pairs(sample_data,10)
    # assert "".join(sample_data.get('template')) == 'NCNBCHB'
    # sample_data = insert_pair(sample_data)
    # assert "".join(sample_data.get('template')) == 'NBCCNBBBCBHCB'
    # sample_data = insert_pair(sample_data)
    # assert "".join(sample_data.get('template')) == 'NBBBCNCCNBBNBNBBCHBHHBCHB'
    # sample_data = insert_pair(sample_data)
    # assert "".join(sample_data.get('template')) == 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
    # sample_data = insert_pair(sample_data)
    # assert len(sample_data.get('template')) == 97
    # sample_data = insert_x_pairs(sample_data, 5)

    sample_counter = count_template(sample_data.get('bigrams'))
    assert sample_counter['B'] == 1749
    assert sample_counter['C'] == 298
    assert sample_counter['H'] == 161
    assert sample_counter['N'] == 865
    # most common - least common
    assert sample_counter.most_common(1)[0][1] - sample_counter.most_common()[-1][1] == 1588
    time_elapsed = time() - start
    print(f'Sample first ten completed in {time_elapsed}')

    start = time()
    sample_data = insert_x_pairs(sample_data, 10)
    time_elapsed = time() - start
    print(f'Sample 20 completed in {time_elapsed}')
    start = time()
    sample_data = insert_x_pairs(sample_data, 10)
    time_elapsed = time() - start
    print(f'Sample 30 completed in {time_elapsed}')
    start = time()
    sample_data = insert_x_pairs(sample_data, 10)
    time_elapsed = time() - start
    print(f'Sample 40 completed in {time_elapsed}')
    sample_counter = count_template(sample_data.get('bigrams'))
    sample_most = sample_counter.most_common(1)[0]
    sample_least = sample_counter.most_common()[-1]
    assert sample_most[0] == 'B'
    assert sample_most[1] == 2192039569602
    assert sample_least[0] == 'H'
    assert sample_least[1] == 3849876073
    assert sample_most[1] - sample_least[1] == 2188189693529

    start = time()

    challenge_data = get_data(INPUT_PATH)
    challenge_data['bigrams'] = build_bigrams(challenge_data.get('template'))
    challenge_data = insert_x_pairs(challenge_data, 10)
    challenge_counter = count_template(challenge_data.get('bigrams'))
    least = challenge_counter.most_common()[-1][1]
    most = challenge_counter.most_common(1)[0][1]
    difference = most - least
    print(f"Part 1: Difference between most and least common is {difference} after 10")
    challenge_data = insert_x_pairs(challenge_data, 30)
    challenge_counter = count_template(challenge_data.get('bigrams'))
    least = challenge_counter.most_common()[-1][1]
    most = challenge_counter.most_common(1)[0][1]
    difference = most - least
    print(f"Part 2: After 40 insertions, difference between most and least common is {difference}")
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