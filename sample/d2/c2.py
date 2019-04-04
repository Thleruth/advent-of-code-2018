def main():

    loaded_array = []
    with open("input.txt") as f:
        for line in f:
            loaded_array.append(line)

    for i in range(0, len(loaded_array)-1):
        for j in range(i+1, len(loaded_array)-2):
            different = 0
            for k in range(0, len(loaded_array[i])):
                if loaded_array[i][k] is not loaded_array[j][k]:
                    different += 1
                if different == 2:
                    break

            if different <= 1:
                for l in range(0, len(loaded_array[i])):
                    if loaded_array[i][l] is not loaded_array[j][l]:
                        print(loaded_array[i][:l] + "*" + loaded_array[i][l+1:])


if __name__ == "__main__":
    main()