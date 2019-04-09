def main():
    with open("input.txt") as f:
        for line in f:
            split_line = line.split(" ")
            player_amount, max_marble = int(split_line[0]), int(split_line[6])

    print(max(playing(player_amount, max_marble)))


def playing(player_amount, max_marble):
    scores = [0] * player_amount
    marbles_placed = [0, 1]
    index_current_marble = 1
    current_player = 2

    for i in range(2, max_marble + 1):
        if i % 23 == 0:
            index_marbles_minus7 = (index_current_marble - 7) % len(marbles_placed)
            scores[current_player-1] += i + marbles_placed[index_marbles_minus7]
            marbles_placed.remove(marbles_placed[index_marbles_minus7])
            index_current_marble = index_marbles_minus7 \
                if index_marbles_minus7 < len(marbles_placed) else len(marbles_placed) - 1
        else:
            size_board = len(marbles_placed)
            index_marble_plus1 = (index_current_marble + 1) % size_board
            index_marble_plus2 = (index_marble_plus1 + 1) % size_board
            if index_marble_plus2 == 0:
                marbles_placed.append(i)
                index_current_marble = size_board
            else:
                marbles_placed.insert(index_marble_plus2, i)
                index_current_marble = index_marble_plus2
        current_player = (current_player + 1) % (player_amount+1) \
            if (current_player + 1) % (player_amount+1) != 0 else 1
    return scores


if __name__ == '__main__':
    main()

