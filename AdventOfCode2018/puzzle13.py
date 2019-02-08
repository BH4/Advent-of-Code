"""
I will have each cart be represented by its location and its velocity vector
which is either (1, 0), (-1, 0), (0, 1), (0, -1)
Each path which is not an intersection can apply a matrix to the velocity
which changed the velocity correctly. for example the \ turn will be a
normal rotation matrix ((0, 1),(1, 0)).

Each cart will have to keep track of weather it will be turning right, left,
or not turning at the next intersection.
The turns can also be accomplished by matrix multiplication.

Note that coordinates are stored as y, x and the y coordinate increases going down.
########## Note that cart positions are stored as y, x but velocities are vx, vy (not actualy necesary. everything stored y, x as long as I swap the right and left turn matricies)
"""
import numpy as np
from copy import deepcopy

# Parse
movement_map = dict()
movement_map[' '] = np.array([[0, 0], [0, 0]])
movement_map['|'] = np.array([[1, 0], [0, 1]])
movement_map['-'] = np.array([[1, 0], [0, 1]])
movement_map['\\'] = np.array([[0, 1], [1, 0]])
movement_map['/'] = np.array([[0, -1], [-1, 0]])


# Left = 0, straight = 1, right = 2
turn_map = [np.array([[0, 1], [-1, 0]]), np.array([[1, 0], [0, 1]]),
            np.array([[0, -1], [1, 0]])]

tracks = []

cart_list = []
y = 0
with open('input/input13.txt') as f:
    for line in f:
        row = []

        for x, character in enumerate(line):
            if character == '^':
                cart = [np.array([y, x]), np.array([-1, 0]), 0]
                row.append('|')
            elif character == 'v':
                cart = [np.array([y, x]), np.array([1, 0]), 0]
                row.append('|')
            elif character == '>':
                cart = [np.array([y, x]), np.array([0, 1]), 0]
                row.append('-')
            elif character == '<':
                cart = [np.array([y, x]), np.array([0, -1]), 0]
                row.append('-')
            elif character == '\n':
                cart = None
            else:
                row.append(character)
                cart = None

            if cart is not None:
                cart_list.append(cart)

        tracks.append(row)
        y += 1


original_cart_list = deepcopy(cart_list)


def print_track(cart_list):
    pcart = dict()
    for i, cart in enumerate(cart_list):
        pos, vel, _ = cart
        pcart[tuple(pos)] = vel

    for y, row in enumerate(tracks):
        s = ''
        for x, character in enumerate(tracks[y]):
            if (y, x) not in pcart:
                s += character
            else:
                s += '*'

        print(s)
    print('\n')


def cart_step(cart):
    pos, vel, turn = cart
    originalPos = tuple(pos)
    originalVel = tuple(vel)
    pos += vel

    t = tracks[pos[0]][pos[1]]
    if t == '+':
        vel = vel.dot(turn_map[turn])
        turn = (turn+1) % 3

        temp = pos+vel
        if tracks[temp[0]][temp[1]] == ' ':
            print(0)
            print(originalPos, originalVel, turn)
    elif t == ' ':
        print('Big error')
        quit()
    else:
        vel = vel.dot(movement_map[t])

        temp = pos+vel
        if tracks[temp[0]][temp[1]] == ' ':
            print(1)
            print(t)
            print(tracks[originalPos[0]-1][originalPos[1]-1], tracks[originalPos[0]-1][originalPos[1]], tracks[originalPos[0]-1][originalPos[1]+1])
            print(tracks[originalPos[0]][originalPos[1]-1], tracks[originalPos[0]][originalPos[1]], tracks[originalPos[0]][originalPos[1]+1])
            print(tracks[originalPos[0]+1][originalPos[1]-1], tracks[originalPos[0]+1][originalPos[1]], tracks[originalPos[0]+1][originalPos[1]+1])
            print(originalPos, originalVel, turn)
            print(pos, vel)

    cart = [pos, vel, turn]
    return cart


def cart_sort(cart_list):
    cart_list.sort(key=lambda x: (x[0][0], x[0][1]))

    return cart_list


def collision_check(cart_list):
    occupied = dict()
    for i, cart in enumerate(cart_list):
        pos = tuple(cart[0])
        if pos in occupied:
            j = occupied[pos]
            return pos, min(i, j), max(i, j)

        occupied[pos] = i

    return None, None, None


def first_crash(cart_list):
    # Return the position of the first crash

    while True:
        cart_list = cart_sort(cart_list)

        for i, cart in enumerate(cart_list):
            cart = cart_step(cart)
            cart_list[i] = cart

            pos, c1, c2 = collision_check(cart_list)
            if pos is not None:
                return (pos[1], pos[0])


def last_cart(cart_list):
    # Return the position of the only cart remaining
    # at the end of the first tick where it is the only cart.

    while True:

        cart_list = cart_sort(cart_list)

        i = 0
        while i < len(cart_list):
            cart = cart_list[i]

            cart = cart_step(cart)
            cart_list[i] = cart

            pos, c1, c2 = collision_check(cart_list)
            if pos is not None:
                cart_list = cart_list[:c1]+cart_list[c1+1:c2]+cart_list[c2+1:]

                if c2 <= i:
                    i -= 2
                elif c1 <= i:
                    i -= 1

            i += 1

        # end of tick
        if len(cart_list) == 1:
            pos = cart_list[0][0]
            return (pos[1], pos[0])


print('Location of the first crash is {}'.format(first_crash(cart_list)))
print('Location of the last cart is {}'.format(last_cart(original_cart_list)))
