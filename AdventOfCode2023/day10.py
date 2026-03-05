
r = 0
s = None
M = []
with open('input/input10.txt') as f:
    for line in f:
        line = line.strip()
        row = [x for x in line]
        if 'S' in row:
            c = row.index('S')
            s = (r, c)

        M.append(row)
        r += 1

# print(len(M), len(M[0]), s)


def add(loc, d):
    return (loc[0]+d[0], loc[1]+d[1])


north = (-1, 0)
east = (0, 1)
south = (1, 0)
west = (0, -1)
direc = [north, east, south, west]

connect = [['7', '|', 'F'],
           ['J', '-', '7'],
           ['L', '|', 'J'],
           ['F', '-', 'L']]


sym_con = dict()
sym_con['7'] = [west, south]
sym_con['J'] = [west, north]
sym_con['L'] = [east, north]
sym_con['F'] = [east, south]
sym_con['|'] = [north, south]
sym_con['-'] = [east, west]


curr = s
# Find connecting locations manually
start_next = []
for i in range(len(direc)):
    check = add(s, direc[i])
    if M[check[0]][check[1]] in connect[i]:
        start_next.append(check)

prev = s
curr = start_next[0]

loop = [start_next[1], s, curr]
steps = 2  # One step for start to curr and one step later for start_next[1] to start
while curr != start_next[1]:
    sym = M[curr[0]][curr[1]]
    next_set = set()
    for d in sym_con[sym]:
        next_set.add(add(curr, d))

    next_set.remove(prev)
    prev = curr
    curr = list(next_set)[0]
    steps += 1

    loop.append(curr)

print(steps//2)



points = set()
for i in range(len(M)):
    for j in range(len(M[0])):
        points.add((i, j))

not_loop = points - set(loop)


# import matplotlib.pyplot as plt
# for i in range(len(loop)-1):
#     plt.plot(*list(zip(loop[i], loop[i+1])), color='k')
# plt.scatter(s[0], s[1], color='b')
# x, y = list(zip(*not_loop))
# plt.scatter(x, y, color='r')
# plt.show()



# Plan:
# Double index values of loop and not_loop to prevent dealing with fractions
# Create extra odd numbered points to close up the newly expanded walls
# Do a bfs from (0, 0) to find all points it can reach which aren't part of the
# loop. These should be the outside.
# Subtract these from not_loop and I should get the interior points

# Doubling and adding between points
loop2 = []
for i in range(len(loop)):
    a = loop[i]
    b = loop[(i+1) % len(loop)]

    mid = (a[0]+b[0], a[1]+b[1])

    loop2.append((a[0]*2, a[1]*2))
    loop2.append(mid)


not_loop2 = set()
for n in not_loop:
    not_loop2.add((n[0]*2, n[1]*2))\


# import matplotlib.pyplot as plt
# for i in range(len(loop2)-1):
#     plt.plot(*list(zip(loop2[i], loop2[i+1])), color='k')
# plt.scatter(s[0]*2, s[1]*2, color='b')
# x, y = list(zip(*not_loop2))
# plt.scatter(x, y, color='r')
# plt.show()

"""
# BFS for outside
loop2_set = set(loop2)
outside = set([(0, 0)])
queue = [(0, 0)]
while len(queue) > 0:
    q = queue.pop(0)
    for d in direc:
        n = add(q, d)

        if len(M)*2 > n[0] >= 0 and len(M[0])*2 > n[1] >= 0:

            if n not in loop2_set and n not in outside:
                outside.add(n)
                queue.append(n)

print(len(not_loop2-outside))


import matplotlib.pyplot as plt
for i in range(len(loop2)-1):
    plt.plot(*list(zip(loop2[i], loop2[i+1])), color='k')
plt.scatter(s[0]*2, s[1]*2, color='b')
x, y = list(zip(*(not_loop2-outside)))
plt.scatter(x, y, color='r')
plt.show()
"""

# BFS for inside
loop2_set = set(loop2)
assert (134, 144) not in loop2_set
inside = set([(134, 144)])
queue = [(134, 144)]
while len(queue) > 0:
    q = queue.pop(0)
    for d in direc:
        n = add(q, d)

        if len(M)*2 > n[0] >= 0 and len(M[0])*2 > n[1] >= 0:

            if n not in loop2_set and n not in inside:
                inside.add(n)
                queue.append(n)

# Count the points that are real not half steps
count = 0
for i in inside:
    if i[0] % 2 == 0 and i[1] % 2 == 0:
        count += 1

print(count)
