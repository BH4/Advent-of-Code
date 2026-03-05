f = open('input/input16.txt')
tiles = f.read().strip().split('\n')
tiles = [[x for x in y] for y in tiles]
f.close()


mirror = dict()
# right, down, left, up
mirror['\\'] = {(0, 1): [(1, 0)], (1, 0): [(0, 1)], (0, -1): [(-1, 0)], (-1, 0): [(0, -1)]}
mirror['/'] = {(0, 1): [(-1, 0)], (1, 0): [(0, -1)], (0, -1): [(1, 0)], (-1, 0): [(0, 1)]}
mirror['-'] = {(0, 1): [(0, 1)], (1, 0): [(0, 1), (0, -1)], (0, -1): [(0, -1)], (-1, 0): [(0, 1), (0, -1)]}
mirror['|'] = {(0, 1): [(1, 0), (-1, 0)], (1, 0): [(1, 0)], (0, -1): [(1, 0), (-1, 0)], (-1, 0): [(-1, 0)]}


def on_board(loc):
    a, b = loc
    return 0 <= a < len(tiles) and 0 <= b < len(tiles[0])


def num_energized(first):
    # first = ((location), (current direction))
    queue = [first]
    used = set(queue)
    while len(queue) > 0:
        loc, direc = queue.pop(0)

        t = tiles[loc[0]][loc[1]]
        if t == '.':
            new_direc = [direc]
        else:
            new_direc = mirror[t][direc]

        for d in new_direc:
            new_loc = (loc[0]+d[0], loc[1]+d[1])
            if on_board(new_loc):
                v = (new_loc, d)
                if v not in used:
                    queue.append(v)
                    used.add(v)

    used_loc = set()
    for u in used:
        used_loc.add(u[0])

    return len(used_loc)


print(num_energized(((0, 0), (0, 1))))

most = 0
for a in range(len(tiles[0])):
    top_start = ((0, a), (1, 0))
    bottom_start = ((len(tiles)-1, a), (-1, 0))

    for s in [top_start, bottom_start]:
        n = num_energized(s)
        most = max(most, n)

for a in range(len(tiles)):
    right_start = ((a, 0), (0, 1))
    left_start = ((a, len(tiles[0])-1), (0, -1))

    for s in [right_start, left_start]:
        n = num_energized(s)
        most = max(most, n)

print(most)
