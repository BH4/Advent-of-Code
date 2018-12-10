"""
Using a deque we follow the game as specified.
Nothing particularly clever here except that the deque structures rotate
function works wonderfully.
"""

from collections import deque


def game(num_players, last_marble):
    circle = deque()
    circle.append(0)

    scores = [0]*num_players

    for i in range(1, last_marble+1):
        if i % 23 != 0:
            circle.rotate(-1)
            circle.append(i)
        else:
            scores[(i-1) % num_players] += i
            circle.rotate(7)
            scores[(i-1) % num_players] += circle.pop()
            circle.rotate(-1)

    return max(scores)


print("Winning elf score for part 1: {}".format(game(448, 71628)))
print("Winning elf score for part 1: {}".format(game(448, 7162800)))
