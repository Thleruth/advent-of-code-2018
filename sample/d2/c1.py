from string import ascii_lowercase

def main():
    preload = {}
    count2 = 0
    count3 = 0
    for c in ascii_lowercase:
        preload[c] = 0

    with open("input.txt") as f:
        for line in f:
            temp = preload.copy()
            for c in line:
                found2 = False
                found3 = False
                if c == '\n':
                    continue
                else:
                    temp[c] = temp[c] + 1
            for c in ascii_lowercase:
                if temp[c] == 2 and not found2:
                    count2 += 1
                    found2 = True
                if temp[c] == 3 and not found3:
                    count3 += 1
                    found3 = True

    print(count2*count3)


if __name__ == "__main__":
    main()

