import numpy as np


class Unit:
    def __init__(self, team, x, y):
        self.team = team
        self.x = x
        self.y = y
        self.health = 200

    def move(self, direction, cavern):
        cavern[self.x][self.y] = 1
        if direction == 0:  # Up
            self.y -= 1
        elif direction == 1:  # Left
            self.x -= 1
        elif direction == 2:  # Right
            self.x += 1
        elif direction == 3:  # Down
            self.y += 1
        cavern[self.x][self.y] = 0
        return cavern

    def print_unit(self):
        print(self.x, self.y, self.team)

def main():
    units = []
    size = 32
    cavern = np.zeros([size, size])

    row = 0
    for line in open("input.txt"):
        for i in range(len(line)):
            value, unit_type = input_to_pathway(ord(line[i]))
            if value != -1:
                cavern[row][i] = value
                if unit_type == 0:
                    units.append(Unit(0, i, row))
                elif unit_type == 1:
                    units.append(Unit(1, i, row))
        row += 1


    for i in range(10):
        print(i, len(units))
        for unit in units:
            if unit.health > 0:
                targets = find_targets(units, (unit.team + 1)%1)
                target, target_distance, direction = find_closest_target(unit, targets, cavern)
                if target is None:
                    print(unit.y, unit.x, "No target reachable")
                    continue
                elif target_distance > 1:
                    print(unit.y, unit.x,"Target found movement on")
                    index_unit = units.index(unit)
                    cavern = unit.move(direction, cavern)
                    units[index_unit] = unit
                if target_distance <= 2:
                    print(unit.y, unit.x, "Attacking time")
                    updated_target_state = attack(target)
                    units[units.index(target)] = updated_target_state
                    if updated_target_state.health <= 0:
                        cavern[updated_target_state.x][updated_target_state.y] = 1
        update_units = []
        for unit in units:
            if unit.health > 0:
                update_units.append(unit)
        update_units.sort(key=lambda u: (u.x, u.y))
        units = update_units

    # todo print map update with position of players and test versus inputs

def find_targets(units, team):
    targets = []
    for unit in units:
        if unit.team == team:
            targets.append(unit)
    return targets

# in spiral way find closest target when found return both the target and its distance
def find_closest_target(unit, targets, cavern):
    # print("start", unit.x, unit.y)
    attackable_target = find_attackable_target(unit, (unit.x, unit.y), targets)
    if attackable_target:
        return attackable_target, 1, None

    move = 0
    size = len(cavern)
    next_positions = [(unit.x, unit.y)]
    visited = []
    while True:
        future_positions = []
        # print(move, next_positions)
        for current_position in next_positions:
            for i in range(4):
                test_position = ""
                if i == 0 and current_position[1] != 0:  # up
                    test_position = (current_position[0], current_position[1] - 1)
                elif i == 1 and current_position[0] != 0:  # left
                    test_position = (current_position[0] - 1, current_position[1])
                elif i == 2 and current_position[1] != size:  # right
                    test_position = (current_position[0] + 1, current_position[1])
                elif i == 3 and current_position[0] != size:  # down
                    test_position = (current_position[0], current_position[1] + 1)
                if test_position and cavern[test_position[1], test_position[0]] == 1:
                    attackable_target = find_attackable_target(unit, (test_position[0], test_position[1]), targets)
                    if attackable_target:
                        return attackable_target, move + 2, None
                    else:
                        if test_position not in visited:
                            future_positions.append(test_position)
                            visited.append(test_position)

        if move == 50:
            exit(13)
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
    for target in targets:
        if target.team != attacker.team:
            distance = abs(coordinate[0] - target.x) + abs(coordinate[1] - target.y)
            if distance == 1:
                return target
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

