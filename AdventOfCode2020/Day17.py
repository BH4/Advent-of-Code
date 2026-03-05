from itertools import product


def get_start(dim):
    active_cubes = set()
    with open('input/input17.txt') as f:
        for i, line in enumerate(f):
            line = line.strip()
            for j, x in enumerate(line):
                if x == '#':
                    if dim == 3:
                        active_cubes.add((i, j, 0))
                    if dim == 4:
                        active_cubes.add((i, j, 0, 0))
    return active_cubes


def neighbors(pos):
    n_list = []
    for p in product([-1, 0, 1], repeat=len(pos)):
        if -1 in p or 1 in p:
            n = tuple([pos[i]+p[i] for i in range(len(pos))])
            n_list.append(n)

    return n_list


def active_neighbors(pos, active):
    count = 0
    for n in neighbors(pos):
        if n in active:
            count += 1
    return count


def next_cycle(state):
    new_state = set()
    pos_to_check = set(x for x in state)
    for p in state:
        pos_to_check |= set(neighbors(p))

    for pos in pos_to_check:
        a = active_neighbors(pos, state)
        if pos in state and (a == 2 or a == 3):
            new_state.add(pos)
        elif pos not in state and a == 3:
            new_state.add(pos)
    return new_state


active_cubes = get_start(3)
for i in range(6):
    active_cubes = next_cycle(active_cubes)
print(len(active_cubes))

active_cubes = get_start(4)
for i in range(6):
    active_cubes = next_cycle(active_cubes)
print(len(active_cubes))
