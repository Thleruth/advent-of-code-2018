import numpy as np
import re
# import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def print(self):
        print(self.x, self.y, self.x_vel, self.y_vel)


with open("input.txt") as f:
    points = []
    for line in f:
        data = re.findall(r'-?\d+', line)
        points.append(Point(int(data[0]), int(data[1]), int(data[2]), int(data[3])))

    size = 400
    max_width = 200

    times = int(size / max_width)
    for i in range(10111, 10161):
        added = 0
        sky_lights = np.full([size, size], " ", dtype=str)
        for point in points:
            x_position = point.x + point.x_vel * i
            y_position = point.y + point.y_vel * i
            if 0 <= x_position <= size - 1 and 0 <= y_position <= size - 1:
                added += 1
                sky_lights[point.x + point.x_vel * i, point.y + point.y_vel * i] = "#"
        # print(i, added)
        if added >= 300:
            print(i, added)

            for j in range(0, times):
                start = 0 + max_width * j
                end = max_width * (j+1)
                for k in range(size):
                    for l in range(start, end):
                        print(sky_lights[k][l], end='')
                    print()
