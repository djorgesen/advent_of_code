class Grid:
    def __init__(self, width=1, height=1):
        self.grid = {}
        self.collisions = 0
        self.points_drawn = 0
        self.segments_applied = 0
        self.total_distance = 0

        def points_with_faults(self):
            return len(self.grid)

    def apply_segment_collisions(self, grid_segment):
        start_point = grid_segment[0]
        end_point = grid_segment[1]
        lower_x, higher_x = (end_point[0], start_point[0]) if end_point[0] < start_point[0] else \
                (start_point[0], end_point[0])
        lower_y, higher_y = (end_point[1], start_point[1]) if end_point[1] < start_point[1] else \
            (start_point[1], end_point[1])
        if start_point[0] > end_point[0]:
            x_multiplier = -1
        else:
            x_multiplier = 1
        if start_point[1] > end_point[1]:
            y_multiplier = -1
        else:
            y_multiplier = 1
        start_x = start_point[0]
        start_y = start_point[1]
        # if start_point[0] != end_point[0] and start_point[1] != end_point[1]:
        #     return
        self.segments_applied += 1
        distance = higher_x - lower_x if higher_x != lower_x else higher_y - lower_y
        self.total_distance += distance
        for current_additive in range(0 , distance + 1):
            if lower_x == higher_x:
                x = start_x
            else:
                x = start_x + current_additive * x_multiplier
            if lower_y == higher_y:
                y = start_y
            else:
                y = start_y + current_additive * y_multiplier
            self.grid[x, y] = self.grid.get((x, y), 0) + 1
            if self.grid[x, y] == 2:
                self.collisions += 1
            self.points_drawn += 1
        last_point = (x,y)


file_read_list =  open('inputs/input_5.txt', 'r').read().split('\n')

max_x = 0
max_y = 0
list_of_segments = []
for line in file_read_list:
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
# nightmare grid
# Grid size is 990 by 990
# There are collisions at 19676 points
# Done!
#
# Process finished with exit code 0




