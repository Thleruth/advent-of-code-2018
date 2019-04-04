import numpy as np


def main():
    loaded_array = []
    # I read the instruction too fast and did a bit of double work for the implementation of the loading but
    # considering it is working I left it that way
    with open("input.txt") as f:
        for line in f:
            separated = line.split(" ")
            location = separated[2][:-1].split(",")
            size = separated[3].split("x")
            start_x = int(location[0])
            end_x = start_x + int(size[0])
            start_y = int(location[1])
            end_y = start_y + int(size[1])
            loaded_array.append(((start_x, start_y), (end_x, end_y)))

    used_inch = np.zeros([1001, 1001], dtype=int)

    for coordinate in loaded_array:
        size_x = coordinate[1][0] - coordinate[0][0]
        size_y = coordinate[1][1] - coordinate[0][1]
        for i in range(1, size_x + 1):
            for j in range(1, size_y + 1):
                current_x = coordinate[0][0] + i
                current_y = coordinate[0][1] + j
                used_inch[current_x][current_y] += 1

    count = 0
    for t in used_inch.flat:
        if t >= 2:
            count += 1

    print(count)


if __name__ == "__main__":
    main()

