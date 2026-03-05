def area_calc(a, b):
    # Used the wrong area formula for a bit.
    # Wrong formula was correct for example and part 1 :')
    return (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)


red_squares = []
with open('input9.txt', 'r') as f:
    for line in f:
        line = line.strip()

        coords = tuple(int(x) for x in line.split(','))
        red_squares.append(coords)


largest_area = 0
for i in range(len(red_squares)-1):
    for j in range(i+1, len(red_squares)):
        area = area_calc(red_squares[i], red_squares[j])
        # area = (1+red_squares[i][0]-red_squares[j][0])*(1+red_squares[i][1]-red_squares[j][1])

        if area > largest_area:
            largest_area = area

print(largest_area)

# Add green squares between each of the red squares
allowed_squares = set()  # includes red squares
for i in range(len(red_squares)):
    a = red_squares[i]
    b = red_squares[(i+1) % len(red_squares)]

    if a[0] == b[0]:
        low = min(a[1], b[1])
        high = max(a[1], b[1])
        for y in range(low, high+1):
            allowed_squares.add((a[0], y))
    elif a[1] == b[1]:
        low = min(a[0], b[0])
        high = max(a[0], b[0])
        for x in range(low, high+1):
            allowed_squares.add((x, a[1]))
    else:
        print('error')
        quit()


def neighbors(curr):
    n_list = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        n = (curr[0]+dx, curr[1]+dy)
        n_list.append(n)
    return n_list


# Find boundary of disallowed squares
# queue = [(6, 1)]
queue = [(40000, 50401)]
disallowed_boundary = set(queue)
while len(queue) > 0:
    curr = queue.pop(0)

    for n in neighbors(curr):
        # check if n is not in the good boundary, but does have neighbors in it
        if n not in allowed_squares and n not in disallowed_boundary:
            ns_neighbors = neighbors(n)
            if any([x in allowed_squares for x in ns_neighbors]):
                disallowed_boundary.add(n)
                queue.append(n)


def intersects(a, b, bad):
    # boundary = set()
    min_x = min(a[0], b[0])
    min_y = min(a[1], b[1])
    max_x = max(a[0], b[0])
    max_y = max(a[1], b[1])

    for x in range(min_x, max_x+1):
        if (x, min_y) in bad or (x, max_y) in bad:
            return True
        # boundary.add((x, min_y))
        # boundary.add((x, max_y))

    for y in range(min_y, max_y+1):
        if (min_x, y) in bad or (max_x, y) in bad:
            return True
        # boundary.add((min_x, y))
        # boundary.add((max_x, y))

    return False
    # return boundary

# If rectangle doesn't contain any of the disallowed boundary then it is valid
# It will only contain any if any are on its boundary
largest_area = 1400081872-1
for i in range(len(red_squares)-1):
    for j in range(i+1, len(red_squares)):
        area = area_calc(red_squares[i], red_squares[j])
        # area = (1+red_squares[i][0]-red_squares[j][0])*(1+red_squares[i][1]-red_squares[j][1])

        if area > largest_area:
            a = red_squares[i]
            b = red_squares[j]
            min_x = min(a[0], b[0])
            min_y = min(a[1], b[1])
            max_x = max(a[0], b[0])
            max_y = max(a[1], b[1])
            if True:#not (max_y > 50401 and min_y < 48337):
                # boundary = get_boundary(red_squares[i], red_squares[j])
                # if len(boundary & disallowed_boundary) == 0:
                if not intersects(a, b, disallowed_boundary):
                    largest_area = area
                    # print(a, b)
                    # print(area)

print(largest_area)
quit()


import matplotlib.pyplot as plt

plt.scatter(*list(zip(*red_squares)))
plt.scatter(*list(zip(*list(disallowed_boundary))))
# plt.scatter(*list(zip(*list(allowed_squares))))
for i in range(len(red_squares)-1):
    plt.plot(*list(zip(red_squares[i], red_squares[i+1])))
plt.show()
