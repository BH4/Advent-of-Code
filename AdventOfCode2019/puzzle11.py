import numpy as np
from intcode_computer import run

with open('input/input11.txt', 'r') as f:
    line = f.readline()

code = [int(x) for x in line.split(',')]


def emergency_hull_painting_robot(code, start_color):
    current_position = (0, 0)
    current_direction = (0, -1)

    stdin = [0]
    white_panels = set()
    modified_panels = set()
    curr = 0
    relative_base = 0

    if start_color == 1:
        white_panels.add(current_position)
        stdin = [1]

    while curr != -1:
        state, out = run(code, stdin, curr=curr, relative_base=relative_base)
        curr, relative_base, code = state

        if curr != -1:
            color = out[0]
            turn = out[1]

            if color == 0:
                if current_position in white_panels:
                    modified_panels.add(current_position)

                if current_position in white_panels:
                    white_panels.remove(current_position)
            elif color == 1:
                if current_position not in white_panels:
                    modified_panels.add(current_position)
                white_panels.add(current_position)

            if turn == 0:
                cd = current_direction
                current_direction = (cd[1], -1*cd[0])
            elif turn == 1:
                cd = current_direction
                current_direction = (-1*cd[1], cd[0])

            current_position = (current_position[0]+current_direction[0], current_position[1]+current_direction[1])

            if current_position in white_panels:
                stdin = [1]
            else:
                stdin = [0]

    return modified_panels, white_panels


copy = [x for x in code]
modified_panels, white_panels = emergency_hull_painting_robot(copy, 0)
print(len(modified_panels))

copy = [x for x in code]
modified_panels, white_panels = emergency_hull_painting_robot(copy, 1)
minx = min([p[0] for p in white_panels])
miny = min([p[1] for p in white_panels])
maxx = max([p[0] for p in white_panels])
maxy = max([p[1] for p in white_panels])

ship = np.zeros((maxy-miny+1, maxx-minx+1), dtype=int)
for p in white_panels:
    ship[p[1]-miny][p[0]-minx] = 1

np.set_printoptions(linewidth=100)
print(ship)
