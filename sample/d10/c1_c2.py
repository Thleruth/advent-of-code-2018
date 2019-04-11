import numpy as np
import re
# try with matplot with import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel


with open("input.txt") as f:
    points = []
    for line in f:
        data = re.findall(r'-?\d+', line)
        points.append(Point(int(data[0]), int(data[1]), int(data[2]), int(data[3])))

    # guessing those numbers with trial and error
    size = 250
    start_try = 1
    end_try = 20000

    for i in range(start_try, end_try):
        print(i)
        sky_lights = np.full([size, size], ".", dtype=str)
        # filling the points in desired checked size
        for point in points:
            x_position = point.x + point.x_vel * i
            y_position = point.y + point.y_vel * i
            if 0 <= x_position <= size - 1 and 0 <= y_position <= size - 1:
                sky_lights[point.x + point.x_vel * i, point.y + point.y_vel * i] = "#"
        points_in_area = np.count_nonzero(sky_lights == "#")
        if points_in_area >= 150:
            print(i, points_in_area)
            for k in range(size):
                for l in range(size):
                    print(sky_lights[l][k], end='')
                print()
