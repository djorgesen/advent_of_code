class Grid:
    def __init__(self, width=1, height=1):
        self.grid = [[0]*height for i in range(width)]
        self.collisions = 0
        self.lines_drawn = 0
    def apply_segment_collisions(self, segment):
        start_point = segment[0]
        end_point = segment[1]
        if start_point[0] != end_point[0] and start_point[1] != end_point[1]:
            return
        self.lines_drawn += 1
        if end_point[0] != start_point[0]:
            lower_number, higher_number = (end_point[0], start_point[0]) if end_point[0] < start_point[0] else \
                (start_point[0], end_point[0])
            for x in range(lower_number - 1 , higher_number):
                self.grid[x][start_point[1]-1] += 1
                if self.grid[x][start_point[1]-1] == 2:
                    self.collisions += 1
        if end_point[1] != start_point[1]:
            lower_number, higher_number = (end_point[1], start_point[1]) if end_point[1] < start_point[1] else \
                (start_point[1], end_point[1])
            for y in range(lower_number - 1, higher_number):
                self.grid[start_point[0]-1][y] += 1
                if self.grid[start_point[0]-1][y] == 2:
                    self.collisions += 1


list =  open('inputs/input_5.txt', 'r').read().split('\n')

max_x = 0
max_y = 0
list_of_segments = []
for line in list:
    segment = line.split('->')
    segment_endpoints = []
    for point in segment:
        xy = point.split(',')
        x = int(xy[0])
        y = int(xy[1])
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
        segment_endpoints.append([x,y])
    list_of_segments.append(segment_endpoints)

vent_field = Grid(max_x, max_y)
for segment in list_of_segments:
    vent_field.apply_segment_collisions(segment)

collisions = vent_field.collisions

print(f'Grid size is {max_x} by {max_y}')
print(f'There are collisions at {collisions} points')

print('Done!')

# output looked like
# Grid size is 990 by 990
# There are collisions at 7414 points
# Done!
#
# Process finished with exit code 0





