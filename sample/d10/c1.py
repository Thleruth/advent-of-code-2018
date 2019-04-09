import numpy as np


size = 1000
used_inch = np.zeros([size, size], dtype=int)
max_width = 200
times = int(size/max_width)
for i in range(0, times):
    start = 0 + max_width * i
    end = max_width * (i+1)
    for j in range(size):
        for k in range(start, end):
            print(used_inch[j][k], end='')
        print()

