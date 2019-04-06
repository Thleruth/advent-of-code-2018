import operator


def main():
    loaded_array = []
    with open("input.txt") as f:
        for line in f:
            split_data = line.split(",")
            x_value = int(split_data[0])
            y_value = int(split_data[1][1:])
            loaded_array.append((x_value, y_value))

    min_x, max_x, min_y, max_y = find_grid_size(loaded_array)

    # to detect the infinite extending ones, I just tested versus a slightly bigger grid
    capture_points_regular = find_capture_points(min_x, max_x, min_y, max_y, loaded_array)
    capture_points_bigger = find_capture_points(min_x-1, max_x+1, min_y-1, max_y+1, loaded_array)
    capture_points_real = {}
    for k, v in capture_points_bigger.items():
        if v == capture_points_regular[k]:
            capture_points_real[k] = v

    best_index = max(capture_points_real.items(), key=operator.itemgetter(1))[0]
    print("The best coordinate has the id #" + str(best_index + 1) +
          " with an area of " + str(capture_points_real[best_index]))


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


def find_capture_points(min_x, max_x, min_y, max_y, coordinates):
    capture_points = {}
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            best_distance = 10000
            best_index = -1
            for k in range(0, len(coordinates)):
                test_distance = cal_distance((i, j), coordinates[k])
                if test_distance == best_distance:
                    best_index = -1
                elif test_distance < best_distance:
                    best_distance = test_distance
                    best_index = k
            try:
                capture_points[best_index] += 1
            except KeyError:
                capture_points[best_index] = 1
    return capture_points


if __name__ == '__main__':
    main()

