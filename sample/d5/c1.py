import sys


def main():
    with open("input.txt") as f:
        for line in f:
            complex_polymer = line
    simple_polymer = deconstruct_without_recursion(list(complex_polymer))
    print("leftover is: " + ''.join(simple_polymer))
    print("length of: " + '' + str(len(simple_polymer)))


# Leave it there for the future, not a clean way of doing and leads to seg fault
def deconstruct_with_recursion(complex_polymer, start):
    sys.setrecursionlimit(50000)
    for i in range(start+1, len(complex_polymer)):
        if complex_polymer[i] == complex_polymer[i-1].swapcase():
            del complex_polymer[i-1]
            del complex_polymer[i-1]
            return deconstruct_with_recursion(complex_polymer, i-2)
    return complex_polymer


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

