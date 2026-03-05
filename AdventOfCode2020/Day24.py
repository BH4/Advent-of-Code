
directions = []
with open('input/input24.txt') as f:
    for line in f:
        directions.append(line.strip())


map_dir_to_move = dict()
map_dir_to_move['e'] = (1, 0)
map_dir_to_move['w'] = (-1, 0)
map_dir_to_move['ne'] = (0, 1)
map_dir_to_move['nw'] = (-1, 1)
map_dir_to_move['se'] = (1, -1)
map_dir_to_move['sw'] = (0, -1)
def direction_to_coord(direction):
    curr = (0, 0)
    while len(direction) > 0:
        if direction[0] in ['e', 'w']:
            d = direction[0]
            direction = direction[1:]
        else:
            d = direction[:2]
            direction = direction[2:]

        move = map_dir_to_move[d]
        curr = (curr[0]+move[0], curr[1]+move[1])
    return curr


flipped = set()
for d in directions:
    pos = direction_to_coord(d)
    if pos in flipped:
        flipped.remove(pos)
    else:
        flipped.add(pos)
print(len(flipped))


def neighbors(pos):
    n_list = []
    for d in map_dir_to_move:
        move = map_dir_to_move[d]
        n_list.append((pos[0]+move[0], pos[1]+move[1]))

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
        if pos in state and (a == 1 or a == 2):
            new_state.add(pos)
        elif pos not in state and a == 2:
            new_state.add(pos)
    return new_state


for i in range(100):
    flipped = next_cycle(flipped)
print(len(flipped))
