def main():
    loaded_array = []
    with open("input.txt") as f:
        for line in f:
            split_data = line.split(",")
            x_value = int(split_data[0])
            y_value = int(split_data[1][1:])
            loaded_array.append((x_value, y_value))

    min_x, max_x, min_y, max_y = find_grid_size(loaded_array)

    count = 0
    boundary = 10000
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            total_distance = 0
            for k in range(0, len(loaded_array)):
                total_distance += cal_distance((i, j), loaded_array[k])
                if total_distance >= boundary:
                    break
                if k == len(loaded_array) - 1:
                    count += 1

    print("the total area is " + str(count))


def cal_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def find_grid_size(coordinates):
    min_x = 1000000
    max_x = 0
    min_y = 1000000
    max_y = 0
    for coordinate in coordinates:
        x_value = coordinate[0]
        y_value = coordinate[1]
        if min_x > x_value:
            min_x = x_value
        if max_x < x_value:
            max_x = x_value
        if min_y > y_value:
            min_y = y_value
        if max_y < y_value:
            max_y = y_value

    return min_x, max_x, min_y, max_y


if __name__ == '__main__':
    main()

