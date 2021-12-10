import time
from collections import deque, Counter

# neat, ripped off from reddit
# def num_fish(fish: list, days: int):
#     f = deque(Counter(fish)[i] for i in range(9))
#     for _ in range(days):
#         z = f.popleft() # remove 9s
#         f[6] += z # add 0s to 6s
#         f.append(z) # re-add the 0s
#     return sum(f)

class LanternfishSchool:
    def __init__(self, list_of_fish_ages):
        self.fish = deque(Counter(list_of_fish_ages)[i] for i in range(9))
        self.days_elapsed = 0

    def age_a_day(self):
        z = self.fish.popleft()  # remove 9s
        self.fish[6] += z  # add 0s to 6s
        self.fish.append(z)  # re-add the 0s


    def total_school_size(self):
        return sum(self.fish)
# sample/test data
# list_of_ages =  open('inputs/input_6.sample.txt', 'r').read().split('\n')[0].split(',')
start = time.time()
list_of_ages =  open('inputs/input_6.txt', 'r').read().split('\n')[0].split(',')
# convert to int
fish = [int(f) for f in list_of_ages]

school = LanternfishSchool(fish)
days = 256

for day in range(days):
    school.age_a_day()

time_elapsed = (time.time() - start)*1000
print(f"After {days} days there are {school.total_school_size()} fish.")
print(f"{time_elapsed} sec have passed.")


# for day in range(176):
#     school.age_a_day()
#
# print(f"After 256 days there are {school.total_school_size()} fish!?!?!")
# # for sample set it should be 5934