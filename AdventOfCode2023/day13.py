import numpy as np

from collections import defaultdict


f = open('input/input13.txt')
note = f.read().strip().split('\n\n')
f.close()


def one_off(a, b):
    """
    Return None if string a and b are not different by exactly one character
    Return index of character otherwise
    """
    ind = None
    for i in range(len(a)):
        if a[i] != b[i]:
            if ind is not None:
                return None
            ind = i

    return ind


def horizontal_reflection_index(note):
    note = note.split('\n')
    check = []  # ind where next ind is same
    inds = []
    for i, x in enumerate(note):
        j = note.index(x)
        if len(inds) > 0 and j == inds[-1]:
            check.append(i-1)
        inds.append(j)

    # print(inds, check)
    result1 = None
    result2 = None
    # print(inds)

    if not (len(set(inds)) == len(note) or len(check) == 0):
        for c in check:
            m = min(c+1, len(note)-(c+1))
            # print(inds)
            # print(c, m, c+1-m, c+1, c+1+m)
            # print(inds[c+1-m:c+1], inds[c+1:c+1+m][::-1])
            # quit()
            if inds[c+1-m:c+1] == inds[c+1:c+1+m][::-1]:
                assert result1 is None
                result1 = c+1

    for c in range(len(note)):
        m = min(c+1, len(note)-(c+1))
        o = one_off(inds[c+1-m:c+1], inds[c+1:c+1+m][::-1])
        if o is not None:
            # lines to check if they are one off
            a = note[c+1-m+o]
            b = note[c+1+m-1-o]
            if o is not None and one_off(a, b) is not None:
                result2 = c+1

    return result1, result2



# print(np.array(note[0]))
# quit()


def transpose(n):
    M = [[x for x in y] for y in n.split('\n')]

    M = np.transpose(np.array(M))

    return '\n'.join([''.join(x) for x in M])


# test = """##.###.
# ..#.#.#
# ..#.#.#
# ##.###.
# .#.####
# ###.###
# .#...#.
# .##...#
# .#.....
# ..#....
# ..#....
# .#....#
# .##...#
# .#...#.
# ###.###"""
# print(horizontal_reflection_index(test))
# quit()



tot = 0
tot2 = 0
for n in note:
    # print('-'*100)
    h, h2 = horizontal_reflection_index(n)

    # print(transpose(n))

    v, v2 = horizontal_reflection_index(transpose(n))

    if h is None and v is None:
        print(n)
        quit()

    if v is None:
        tot += 100*h
    elif h is None:
        tot += v
    else:
        quit()

    # print(h2, v2)

    if h2 is None and v2 is None:
        print(n)
        quit()

    if v2 is None:
        tot2 += 100*h2
    elif h2 is None:
        tot2 += v2
    else:
        quit()

print(tot)
print(tot2)
