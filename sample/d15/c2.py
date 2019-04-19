import numpy as np
from operator import attrgetter


class Unit:
    def __init__(self, team, x, y, power):
        self.team = team
        self.x = x
        self.y = y
        self.health = 200
        self.power = power

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
    power = 4
    while True:
        win = play(power)
        if win:
            break
        power += 1


def play(power):
    file = "input.txt"
    units = []
    for line in open(file):
        size = len(line)
        break
    cavern = np.zeros([size, size])

    row = 0
    for line in open(file):
        for i in range(len(line)):
            value, unit_type = input_to_pathway(ord(line[i]))
            if value != -1:
                cavern[row][i] = value
                if unit_type >= 0:
                    if unit_type == 0:
                        units.append(Unit(unit_type, i, row, 3))
                    else:
                        units.append(Unit(unit_type, i, row, power))
        row += 1

    unit_count = [0, 0]
    for unit in units:
        unit_count[unit.team] += 1
    starting_elves = unit_count[1]

    for i in range(1000):
        for unit in units:
            if unit.health > 0:
                if unit_count[1] < starting_elves:
                    return False
                if unit_count[0] == 0:
                    health = 0
                    for test in units:
                        if test.health > 0:
                            health += test.health
                    print(i, health, i * health)
                    return True
                targets = find_targets(units, (unit.team + 1)%2)
                target, target_distance, direction = find_closest_target(unit, targets, cavern)
                if target is None:
                    continue
                elif target_distance > 1:
                    index_unit = units.index(unit)
                    cavern = unit.move(direction, cavern)
                    units[index_unit] = unit
                if target_distance <= 2:
                    updated_target_state = attack(target, unit.power)
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


def find_targets(units, team):
    targets = []
    for unit in units:
        if unit.team == team:
            targets.append(unit)
    return targets


def find_closest_target(unit, targets, cavern):

    attackable_target = find_attackable_target((unit.x, unit.y), targets)
    if attackable_target:
        return attackable_target, 1, None

    move = 0
    size = len(cavern)
    next_positions = [(-1, (unit.x, unit.y))]
    visited = []
    while True:
        future_positions = []
        potential_attack_positions = []
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
                    attackable_target = find_attackable_target((test_position[0], test_position[1]), targets)
                    if attackable_target:
                        potential_attack_positions.append((initial_movement, test_position))
                    else:
                        if test_position not in visited and len(potential_attack_positions) == 0:
                            future_positions.append((initial_movement, test_position))
                            visited.append(test_position)

        if len(potential_attack_positions) > 0:
            potential_attack_positions.sort(key=lambda p: (p[1][1], p[1][0]))
            best_attack_position = potential_attack_positions[0]
            attackable_target = find_attackable_target(best_attack_position[1], targets)
            return attackable_target, move + 2, best_attack_position[0]

        if len(future_positions) == 0:
            return None, None, None

        next_positions = future_positions
        move += 1


def find_attackable_target(coordinate, targets):
    potential_targets = []
    for target in targets:
        distance = abs(coordinate[0] - target.x) + abs(coordinate[1] - target.y)
        if distance == 1 and target.health > 0:
            potential_targets.append(target)
    if len(potential_targets) > 0:
        potential_targets.sort(key=lambda t: (t.y, t.x))
        return min(potential_targets, key=attrgetter('health'))
    return None


def find_optimal_distance(unit, target):
    return abs(unit[0] - target[0]) + abs(unit[1] - target[1])


def attack(target, power):
    target.health -= power
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
    return int(value), unit_type


if __name__ == '__main__':
    main()

