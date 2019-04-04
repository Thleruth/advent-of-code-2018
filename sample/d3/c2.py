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

    # loading the inch utilizaion
    for coordinate in loaded_array:
        size_x = coordinate[1][0] - coordinate[0][0]
        size_y = coordinate[1][1] - coordinate[0][1]
        for i in range(1, size_x + 1):
            for j in range(1, size_y + 1):
                current_x = coordinate[0][0] + i
                current_y = coordinate[0][1] + j
                used_inch[current_x][current_y] += 1

    # checking which case only use 1 on all square
    # Alternatively  I could have made it shorter by stopping as soon as any utilization above 1 is found
    for i in range(0, len(loaded_array)):
        count = 0
        coordinate = loaded_array[i]
        size_x = coordinate[1][0] - coordinate[0][0]
        size_y = coordinate[1][1] - coordinate[0][1]
        area = size_x * size_y
        for j in range(1, size_x + 1):
            for k in range(1, size_y + 1):
                current_x = coordinate[0][0] + j
                current_y = coordinate[0][1] + k
                count += used_inch[current_x][current_y]

        if count == area:
            print("Valid claim #" + str(i + 1))
            break


if __name__ == "__main__":
    main()

