class Position:
    def __init__(self, horizontal=0, depth=0, aim=0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def down(self, distance):
        self.aim += distance

    def up(self, distance):
        self.aim -= distance

    def forward(self, distance):
        self.horizontal += distance
        self.depth += self.aim * distance

    def __str__(self):
        return f'h: {self.horizontal}, d: {self.depth}, a: {self.aim}'

position = Position()

list = []
with open('inputs/input_day_2.txt', 'r') as day_1_file:
    list = day_1_file.read().split('\n')
commands = [item.split() for item in list]
failed_commands = []
for index, line in enumerate(commands):
    command = line[0]
    distance = int(line[1])
    if command == 'down':
        position.down(distance)
    elif command == 'up':
        position.up(distance)
    elif command == 'forward':
        position.forward(distance)
    else:
        dummy = {
            'command':command,
            'distance': distance,
            'index': index
        }
        failed_commands.append(dummy)
print(f'The final position is {position}')
product = position.depth * position.horizontal
print(f'The product is {product}')
print('Done!')

# output looked like
# The final position is h: 1890, d: 986622, a: 1172
# The product is 1864715580
# Done!
#
# Process finished with exit code 0