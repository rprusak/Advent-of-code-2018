import sys
from typing import List
from collections import defaultdict


def calculate_winner_score(players_count: int, last_marble_value: int):
    marbles = [0]
    current_marble_index = 0
    player_scores = defaultdict(int)
    current_player = 0

    for marble_value in range(1, last_marble_value + 1):
        current_player = (current_player + 1) % players_count

        if (marble_value % 23) != 0:
            if len(marbles) == 1:
                marbles.append(marble_value)
                current_marble_index = 1
            elif current_marble_index == len(marbles) - 1:
                current_marble_index = 1
                marbles.insert(current_marble_index, marble_value)
            elif current_marble_index == len(marbles) - 2:
                marbles.append(marble_value)
                current_marble_index = len(marbles) - 1
            else:
                current_marble_index += 2
                marbles.insert(current_marble_index, marble_value)
        else:
            player_scores[current_player] += marble_value

            current_marble_index = (current_marble_index - 7) % len(marbles)
            player_scores[current_player] += marbles[current_marble_index]
            del marbles[current_marble_index]
            current_marble_index %= len(marbles)

        # print_marbles(marbles, current_marble_index)

    return player_scores[max(player_scores, key=player_scores.get)]


def print_marbles(marbles: List[int], current_marble_index: int):
    for i in range(0, len(marbles)):
        if i != current_marble_index:
            print("%4d" % marbles[i], end="")
        else:
            print("(%2d)" % marbles[i], end="")
    print()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: <players count> <last marble value>")
        exit()

    print(calculate_winner_score(int(sys.argv[1]), int(sys.argv[2])))
