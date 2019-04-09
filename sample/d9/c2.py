class MarbleNode:
    def __init__(self, data, last, next):
        self.data = data
        self.last = last
        self.next = next


def main():
    with open("input.txt") as f:
        for line in f:
            split_line = line.split(" ")
            player_amount, max_marble = int(split_line[0]), int(split_line[6])

    print(max(playing(player_amount, max_marble*100)))


def playing(player_amount, max_marble):
    m0 = MarbleNode(0, None, None)
    m1 = MarbleNode(1, m0, m0)
    m0.last, m0.next = m1, m1

    scores = [0] * player_amount
    current_marble_node = m1
    current_player = 2

    for i in range(2, max_marble + 1):
        if i % 23 == 0:
            remove_marble_node = current_marble_node.last.last.last.last.last.last.last
            scores[current_player-1] += i + remove_marble_node.data
            remove_marble_node.last.next = remove_marble_node.next
            current_marble_node = remove_marble_node.next
            remove_marble_node.last, remove_marble_node.next = None, None  # For garbage collection
        else:
            new_marble_node = MarbleNode(i, current_marble_node.next, current_marble_node.next.next)
            current_marble_node.next.next.last = new_marble_node
            current_marble_node.next.next = new_marble_node
            current_marble_node = new_marble_node
        current_player = (current_player + 1) % (player_amount+1) \
            if (current_player + 1) % (player_amount+1) != 0 else 1
    return scores


if __name__ == '__main__':
    main()

