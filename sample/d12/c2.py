def main():
    flowers = ""
    changes = {}
    for line in open("input.txt"):
        if len(line) > 15:
            flowers = line[15:-1]
        elif len(line) > 5:
            split = line.split(" ")
            changes[split[0]] = split[2].strip()

    extra_left = 0
    generations = 50000000000
    for i in range(generations):
        old_state = flowers
        old_extra_left = extra_left
        flowers, extra_left = evolve(flowers, changes, extra_left)
        if old_state == flowers:
            extra_left = extra_left + (extra_left - old_extra_left) * (generations - (i + 1))
            break
    print(flowers, find_score(flowers, extra_left))


def evolve(flowers, changes, extra_left):

    needed_buffer_left, needed_buffer_right = calculate_buffers(flowers)

    flowers = ("." * needed_buffer_left) + flowers + ("." * needed_buffer_right)
    magic_sequences = changes.keys()

    transformations = {}
    for i in range(2, len(flowers) - 2):
        test_sequence = flowers[i-2:i+3]
        if test_sequence in magic_sequences:
            transformations[i] = changes[test_sequence]

    for t, v in transformations.items():
        index = t
        flowers = flowers[:index] + v + flowers[index+1:]

    flowers, remove_left = reduce_flowers(flowers)
    extra_left += needed_buffer_left - remove_left
    return flowers, extra_left


def calculate_buffers(flowers):
    flowers_size = len(flowers)
    needed_buffer_left = 5
    if flowers[0] == ".":
        needed_buffer_left -= 1
        if flowers[1] == ".":
            needed_buffer_left -= 1
            if flowers[2] == ".":
                needed_buffer_left -= 1
                if flowers[3] == ".":
                    needed_buffer_left -= 1
                    if flowers[4] == ".":
                        needed_buffer_left -= 1
    needed_buffer_right = 5
    if flowers[flowers_size - 1] == ".":
        needed_buffer_right -= 1
        if flowers[flowers_size - 2] == ".":
            needed_buffer_right -= 1
            if flowers[flowers_size - 3] == ".":
                needed_buffer_right -= 1
                if flowers[flowers_size - 4] == ".":
                    needed_buffer_right -= 1
                    if flowers[flowers_size - 5] == ".":
                        needed_buffer_right -= 1

    return needed_buffer_left, needed_buffer_right


def reduce_flowers(flowers):
    start = 0
    for i in range(0, len(flowers)):
        if flowers[i] == ".":
            start = i
        else:
            break
    end = 0
    for i in range(len(flowers)-1, -1, -1):
        if flowers[i] == ".":
            end = i
        else:
            break

    return flowers[start+1:end], start+1


def find_score(flowers, extra_left):
    score = 0
    for i in range(0, len(flowers)):
        if flowers[i] == "#":
            score += i - extra_left
    return score


if __name__ == '__main__':
    main()
