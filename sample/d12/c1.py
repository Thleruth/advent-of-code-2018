# todo refactor state for flowers
# todo clean up 

def main():
    state = ""
    changes = {}
    for line in open("input.txt"):
        if len(line) > 15:
            state = line[15:-1]
        elif len(line) > 5:
            split = line.split(" ")
            changes[split[0]] = split[2].strip()

    extra_left = 0
    generations = 10000 # should try 50billion gen but want to test if there is no state evol and stop it short
    for i in range(generations):
        print(state)
        old_state = state
        state, extra_left = evolve(state, changes, extra_left)
        if old_state == state:
            print(i) # todo check if same pattern must moving to right if so forecast the change in 50b year
            break

    print(state, find_score(state, extra_left))


def evolve(state, changes, extra_left):

    needed_buffer_left, needed_buffer_right = calculate_buffers(state)

    state = ("." * needed_buffer_left) + state + ("." * needed_buffer_right)
    magic_sequences = changes.keys()

    transformations = {}
    for i in range(2, len(state) - 2):
        test_sequence = state[i-2:i+3]
        if test_sequence in magic_sequences:
            transformations[i] = changes[test_sequence]

    for t, v in transformations.items():
        index = t
        state = state[:index] + v + state[index+1:]

    # state, remove_left = reduce_state(state)
    # extra_left += needed_buffer_left - remove_left
    extra_left += needed_buffer_left
    return state, extra_left


def calculate_buffers(state):
    state_size = len(state)
    needed_buffer_left = 5
    if state[0] == ".":
        needed_buffer_left -= 1
        if state[1] == ".":
            needed_buffer_left -= 1
            if state[2] == ".":
                needed_buffer_left -= 1
                if state[3] == ".":
                    needed_buffer_left -= 1
                    if state[4] == ".":
                        needed_buffer_left -= 1
    needed_buffer_right = 5
    if state[state_size - 1] == ".":
        needed_buffer_right -= 1
        if state[state_size - 2] == ".":
            needed_buffer_right -= 1
            if state[state_size - 3] == ".":
                needed_buffer_right -= 1
                if state[state_size - 4] == ".":
                    needed_buffer_right -= 1
                    if state[state_size - 5] == ".":
                        needed_buffer_right -= 1

    return needed_buffer_left, needed_buffer_right


def reduce_state(state):
    start = 0
    for i in range(0, len(state)):
        if state[i] == ".":
            start = i
        else:
            break
    end = 0
    for i in range(len(state)-1, -1, -1):
        if state[i] == ".":
            end = i
        else:
            break

    return state[start+1:end], start+1


def find_score(state, extra_left):
    score = 0
    for i in range(0, len(state)):
        if state[i] == "#":
            score += i - extra_left
    return score

if __name__ == '__main__':
    main()
