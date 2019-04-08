def main():
    loaded_array = []
    with open("test.txt") as f:
        for line in f:
            loaded_array = line.split(" ")
    # start this way as the start is like 1 child and no meta
    data, meta_data = analyse(loaded_array, 1, [])

    # actually did not have to collect all the meta
    total = 0
    for i in meta_data:
        total += int(i)
    print(total)

def analyse(data, child_amount, meta_data):
    for i in range(0, child_amount):
        new_child_amount, new_meta_data_amount = int(data[0]), int(data[1])
        data, meta_data = analyse(data[2:], new_child_amount, meta_data)
        for j in range(0, new_meta_data_amount):
            temp_meta = data[0]
            meta_data.append(temp_meta)
            data.remove(temp_meta)
    return data, meta_data


if __name__ == '__main__':
    main()

