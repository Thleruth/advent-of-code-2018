import numpy as np
from operator import attrgetter


# A OK
# B OK
# 1 Ok
# 2 Ok
# 3 ok
# 4 ok
# 5 ok
# All tests are passing but still off due to the mis-choice of target when multiple targets are within same distance
# issue is that I test up, left, right, down but when the movement is more than one technically up/down < left/up
# Thus the order is not correct. Positions need to be consolidated and tested while all gather for the movement level
class Unit:
    def __init__(self, team, x, y):
        self.team = team
        self.x = x
        self.y = y
        self.health = 200

    def move(self, direction, cavern):
        cavern[self.y][self.x] = 1
        if direction == 0:  # Up
            self.y -= 1
        elif direction == 1:  # Left
            self.x -= 1
        elif direction == 2:  # Right
            self.x += 1
        elif direction == 3:  # Down
            self.y += 1
        cavern[self.y][self.x] = 0
        return cavern

    def print_unit(self):
        print(self.x, self.y, self.team, self.health)

def main():
    file = "input.txt"
    units = []
    for line in open(file):
        size = len(line)
    cavern = np.zeros([size, size])

    row = 0
    for line in open(file):
        for i in range(len(line)):

            value, unit_type = input_to_pathway(ord(line[i]))
            if value != -1:
                cavern[row][i] = value
                if unit_type >= 0:
                    units.append(Unit(unit_type, i, row))
        row += 1

    unit_count = [0, 0]
    for unit in units:
        unit_count[unit.team] += 1

    for i in range(1000):
        # print(i, len(units))
        print("start round #", i + 1)
        for unit in units:
            # print("play", (unit.y, unit.x, unit.team, unit.health))
            if unit.health > 0:
                if unit_count[0] == 0 or unit_count[1] == 0:
                    print(unit_count)
                    health = 0
                    full_round = i
                    for test in units:
                        if test.health > 0:
                            print(test.health)
                            health += test.health
                    print(full_round, health, full_round * health)
                    exit(1)
                targets = find_targets(units, (unit.team + 1)%2)
                target, target_distance, direction = find_closest_target(unit, targets, cavern)
                if target is None:
                    # print(unit.y, unit.x, "No target reachable")
                    continue
                elif target_distance > 1:
                    # print(unit.y, unit.x, "Target found movement on")
                    index_unit = units.index(unit)
                    cavern = unit.move(direction, cavern)
                    units[index_unit] = unit
                if target_distance <= 2:
                    # print(unit.x, unit.y, "Attacking time on ", (target.x, target.y, target.health))
                    updated_target_state = attack(target)
                    # print(updated_target_state.y, updated_target_state.y, updated_target_state.health)
                    units[units.index(target)] = updated_target_state
                    if updated_target_state.health <= 0:
                        unit_count[updated_target_state.team] -= 1
                        cavern[updated_target_state.y][updated_target_state.x] = 1

        update_units = []

        for unit in units:
            if unit.health > 0:
                update_units.append(unit)
        update_units.sort(key=lambda u: (u.y, u.x))
        units = update_units

        for unit in update_units:
            unit.print_unit()
        for r in range(len(cavern)):
            for c in range(len(cavern[r])):
                found = False
                for unit in units:
                    if unit.y == r and unit.x == c:
                        if unit.team == 1:
                            print("E", end="")
                            found = True
                        else:
                            print("G", end="")
                            found = True
                if not found:
                    if cavern[r][c] == 0:
                        print("#", end ="")
                    else:
                        print(".", end="")
            print()

        print("###############")

def find_targets(units, team):
    targets = []
    for unit in units:
        if unit.team == team:
            targets.append(unit)
    return targets

# in spiral way find closest target when found return both the target and its distance
def find_closest_target(unit, targets, cavern):
    attackable_target = find_attackable_target(unit, (unit.x, unit.y), targets)
    if attackable_target:
        return attackable_target, 1, None

    move = 0
    size = len(cavern)
    next_positions = [(-1, (unit.x, unit.y))]
    visited = []
    while True:
        future_positions = []
        for current_position in next_positions:
            coordinate = current_position[1]
            for i in range(4):
                test_position = ""
                if move == 0:
                    initial_movement = i
                else:
                    initial_movement = current_position[0]
                if i == 0 and current_position[1] != 0:  # up
                    test_position = (coordinate[0], coordinate[1] - 1)
                elif i == 1 and coordinate[0] != 0:  # left
                    test_position = (coordinate[0] - 1, coordinate[1])
                elif i == 2 and coordinate[1] != size:  # right
                    test_position = (coordinate[0] + 1, coordinate[1])
                elif i == 3 and coordinate[0] != size:  # down
                    test_position = (coordinate[0], coordinate[1] + 1)

                if test_position and cavern[test_position[1], test_position[0]] == 1:
                    attackable_target = find_attackable_target(unit, (test_position[0], test_position[1]), targets)
                    if attackable_target:
                        return attackable_target, move + 2, initial_movement
                    else:
                        if test_position not in visited:
                            future_positions.append((initial_movement, test_position))
                            visited.append(test_position)

        if len(future_positions) == 0:
            return None, None, None
        next_positions = future_positions
        move += 1


    # optimal_choices = []
    # for target in targets:
    #     optimal_distance = find_optimal_distance((unit.x, unit.y), (target.x, target.y))
    #     if optimal_distance == 1:
    #         return target, optimal_distance, None
    #     optimal_choices.append((optimal_distance, target))
    # optimal_choices.sort(key=lambda a: a[0])
    #
    # for optimal_choice in optimal_choices:
    #     target = optimal_choice[1]
    #     corners = [(target.x, target.y+1), (target.x-1, target.y), (target.x+1, target.y), (target.x, target.y-1)]
    #     optimal_corners = []
    #     for corner in corners:
    #         if cavern[corner[0], corner[1]] == 1:
    #             optimal_distance = find_optimal_distance((unit.x, unit.y), (corner[0], corner[1]))
    #             optimal_corners.append((optimal_distance, corner))
    #     optimal_corners.sort(key=lambda a: a[0])
    #
    #     best_real_distance = 100
    #     for optimal_corner in optimal_corners:
    #         continue
    #         # find real distance
    #         # test if better than optinal of next if so break, if not continue and prove (short cut test..)
    #
    #     # test if best real better than optimal of second choice if so break, if not test -> Might need an extra var
    #
    #     # t_d will +1 corner distance

def find_attackable_target(attacker, coordinate, targets):
    potential_targets = []
    for target in targets:
        if target.team != attacker.team:
            distance = abs(coordinate[0] - target.x) + abs(coordinate[1] - target.y)
            if distance == 1 and target.health > 0:
                potential_targets.append(target)
    if len(potential_targets) > 0:
        potential_targets.sort(key=lambda t: (t.y, t.x))
        # if coordinate[0] == 23 and coordinate[1] == 18:
        #     for potential_target in potential_targets:
        #         potential_target.print_unit()
        return min(potential_targets, key=attrgetter('health'))
    return None


def find_optimal_distance(unit, target):
    return abs(unit[0] - target[0]) + abs(unit[1] - target[1])


def attack(target):
    target.health -= 3
    return target



def input_to_pathway(char):
    value = -1
    unit_type = -1
    if char == 10:
        pass
    elif char == 35:
        value = 0
    elif char == 46:
        value = 1
    elif char == 71:  # G
        value = 0
        unit_type = 0
    elif char == 69:  # E
        value = 0
        unit_type = 1
    # else:
    #     print(chr(char))
    #     print(char)
    return int(value), unit_type


if __name__ == '__main__':
    main()

    # for i in cavern:
    #     for j in i:
    #         print(int(j), end="")
    #     print()
    # for elf in elfs:
    #     print(elf.x, elf.y)
    #
    # print("GOB")
    # for goblin in goblins:
    #     print(goblin.x, goblin.y)


    # for each units
    # Find targets check if any is in range skip next step
    # if not find shortest to all targets, move on cell
    # if distance was 2 or 1 attack

