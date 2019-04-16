import numpy as np


class Cart:
    def __init__(self, x, y, direction, cross_passed):
        self.x = x
        self.y = y
        self.position_score = x + 151 * y
        self.direction = direction
        self.cross_passed = cross_passed


def main():
    carts = []
    pathways = np.zeros([151, 151])

    row = 0
    for line in open("input.txt"):
        for i in range(len(line)):
            value, cart_direction = input_to_pathway(ord(line[i]))
            pathways[row][i] = value
            if cart_direction != -1:
                carts.append(Cart(i, row, cart_direction, 0))
        row += 1

    while True:
        new_carts = []
        old_carts = carts.copy()
        for cart in carts:
            old_carts.remove(cart)
            moved_cart = move(pathways, cart)
            for old_cart in old_carts:
                if moved_cart.position_score == old_cart.position_score:
                    print("Crash at: ", (moved_cart.x, moved_cart.y))
                    exit(1)
            for new_cart in new_carts:
                if moved_cart.position_score == new_cart.position_score:
                    print("Crash at:", (cart.x, cart.y))
                    exit(1)
            new_carts.append(moved_cart)
        new_carts.sort(key=lambda x: x.position_score)
        carts = new_carts


def input_to_pathway(char):
    value = -1
    cart_direction = -1
    if char in [10, 32]:
        value = 0
    elif char in [45, 124]:
        value = 1
    elif char == 60:  # <
        value = 1
        cart_direction = 3
    elif char == 62:  # >
        value = 1
        cart_direction = 1
    elif char == 94:  # ^
        value = 1
        cart_direction = 0
    elif char == 118:  # v
        value = 1
        cart_direction = 2
    elif char == 47:  # /
        value = 2
    elif char == 92:  # \
        value = 3
    elif char == 43:
        value = 4
    return int(value), cart_direction


def move(pathways, cart):
    y_pos = cart.y
    x_pos = cart.x
    cart_direction = cart.direction
    cross_passed = cart.cross_passed
    path_type = pathways[y_pos][x_pos]
    if path_type == 1:
        pass
    elif path_type == 2:
        if cart_direction%2 == 0:
            cart_direction = (cart_direction + 1)%4
        else:
            cart_direction = (cart_direction - 1)%4
    elif path_type == 3:
        if cart_direction%2 == 0:
            cart_direction = (cart_direction - 1)%4
        else:
            cart_direction = (cart_direction + 1)%4
    elif path_type == 4:
        cart_direction = (cart_direction + cross_passed%3 - 1)%4
        cross_passed += 1
    if cart_direction == 0:  # North
        y_pos -= 1
    elif cart_direction == 1:  # East
        x_pos += 1
    elif cart_direction == 2:  # South
        y_pos += 1
    elif cart_direction == 3:  # West
        x_pos -= 1
    return Cart(x_pos, y_pos, cart_direction, cross_passed)


if __name__ == '__main__':
    main()

