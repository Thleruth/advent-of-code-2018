import string


def main():
    with open("input.txt") as f:
        for line in f:
            complex_polymer = line
    size = len(complex_polymer)
    best_removal = "fail"
    for char in string.ascii_lowercase:
        modified_polymer = complex_polymer.replace(char, "").replace(char.upper(), "")
        test_polymer = deconstruct_without_recursion(modified_polymer)
        test_size = len(test_polymer)
        if size > test_size:
            size = test_size
            best_removal = char
    print("Best size is " + str(size) + " by removing " + best_removal)


def deconstruct_without_recursion(complex_polymer):
    temp = []
    for char in complex_polymer:
        if temp and char == temp[-1].swapcase():
            temp.pop()
        else:
            temp.append(char)
    return ''.join(temp)


if __name__ == '__main__':
    main()

