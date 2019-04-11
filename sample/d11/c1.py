import numpy as np


def main():
    serial = 0
    for line in open("input.txt"):
        serial = int(line)
    hologram = load_hologram(serial)

    print(find_power_sub_grid(hologram, 3))


def find_power_sub_grid(hologram, size):
    best_index = (0, 0)
    best_power = 0
    for i in range(1, 301 - size):
        for j in range(1, 301 - size):
            test_power = 0
            for k in range(pow(size, 2)):
                test_power += hologram[i + k % size][j + int(k / size)]
            if test_power > best_power:
                best_power, best_index = test_power, (i, j, size)
    return best_power, best_index


def load_hologram(serial):
    grid = np.empty([301, 301])
    for i in range(1, 301):
        for j in range(1, 301):
            grid[i][j] = int(str(((i + 10) * j + serial) * (i + 10))[:-2][-1]) - 5
    return grid


if __name__ == '__main__':
    main()

