from bisect import bisect


f = open('input/test.txt')
weights = f.read().strip().split('\n')
weights = [[int(x) for x in y] for y in weights]
f.close()


def on_board(loc):
    a, b = loc
    return 0 <= a < len(weights) and 0 <= b < len(weights[0])


def allowed_moves(direc, d_count):
    all_direc = set([(0, 1), (0, -1), (1, 0), (-1, 0)])
    if direc in all_direc:
        all_direc.remove((direc[0]*-1, direc[1]*-1))

        if d_count >= 3:
            all_direc.remove(direc)
    return all_direc


def weight_index_find(w, q):
    def f(x):
        return x[1]

    return bisect(q, w, key=f)


# first = ((location), current weight, last direction, number of times that direction was used)
first = ((0, 0), 0, (0, 0), 0, ())
queue = [first]
used = dict()  # minimum current weight when reaching each node.
while len(queue) > 0:
    loc, curr_weight, direc, d_count, moves = queue.pop(0)
    print(loc)

    # print([x[1] for x in queue])

    if loc == (len(weights)-1, len(weights[0])-1):
        break

    new_direc = allowed_moves(direc, d_count)
    for d in new_direc:
        new_loc = (loc[0]+d[0], loc[1]+d[1])
        if on_board(new_loc):
            w = weights[new_loc[0]][new_loc[1]]
            new_d_count = 1
            if d == direc:
                new_d_count = d_count+1

            v = (new_loc, curr_weight+w, d, new_d_count, tuple(list(moves)+[new_loc]))
            if new_loc not in used or used[(new_loc, direc, d_count)] >= curr_weight+w:
                used[(new_loc, direc, d_count)] = curr_weight+w
                queue.insert(weight_index_find(curr_weight+w, queue), v)



print(curr_weight)
print(moves)
