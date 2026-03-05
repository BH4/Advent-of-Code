from collections import defaultdict


seats = []
with open('input/input11.txt') as f:
    # floor = -1, empty = 0, occupied = 1
    for line in f:
        row = []
        for i in line.strip():
            if i == '.':
                row.append(-1)
            elif i == 'L':
                row.append(0)
            else:
                print('missed some', i)
        seats.append(row)

"""
def count_neighbors(seats, i, j):
    count = 0
    for di in range(-1, 2):
        if 0 <= i+di < len(seats):
            for dj in range(-1, 2):
                if 0 <= j+dj < len(seats[i]):
                    if not (di == 0 and dj == 0):
                        s = seats[i+di][j+dj]
                        if s == 1:
                            count += 1
    return count


def step(seats):
    new_seats = []
    changes = 0
    for i in range(len(seats)):
        row = []
        for j in range(len(seats[i])):
            s = seats[i][j]
            if s >= 0:
                c = count_neighbors(seats, i, j)
                if c == 0 and s == 0:
                    row.append(1)
                    changes += 1
                elif c >= 4 and s == 1:
                    row.append(0)
                    changes += 1
                else:
                    row.append(s)
            else:
                row.append(-1)
        new_seats.append(row)
    return new_seats, changes


original_seats = seats
changes = 1
steps = 0
while changes > 0:
    seats, changes = step(seats)
    steps += 1

print(sum([row.count(1) for row in seats]))
"""


def find_neighbors(seats, nearest=True):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbor_dict = defaultdict(list)
    length = len(seats)
    width = len(seats[0])
    for i in range(length):
        for j in range(width):
            for d in directions:
                if nearest:
                    n = (i+d[0], j+d[1])
                else:
                    n = (i+d[0], j+d[1])
                    while ((0 <= n[0] < length and 0 <= n[1] < width) and
                            seats[n[0]][n[1]] == -1):
                        n = (n[0]+d[0], n[1]+d[1])

                if 0 <= n[0] < length and 0 <= n[1] < width:
                    if seats[n[0]][n[1]] != -1:
                        neighbor_dict[(i, j)].append((n[0], n[1]))
    return neighbor_dict


def count_neighbors(seats, i, j, neighbor_dict):
    count = [seats[n[0]][n[1]] for n in neighbor_dict[(i, j)]].count(1)
    return count


def step(seats, neighbor_dict, limit):
    new_seats = []
    changes = 0
    for i in range(len(seats)):
        row = []
        for j in range(len(seats[i])):
            s = seats[i][j]
            if s >= 0:
                c = count_neighbors(seats, i, j, neighbor_dict)
                if c == 0 and s == 0:
                    row.append(1)
                    changes += 1
                elif c >= limit and s == 1:
                    row.append(0)
                    changes += 1
                else:
                    row.append(s)
            else:
                row.append(-1)
        new_seats.append(row)
    return new_seats, changes


original_seats = seats
changes = 1
steps = 0
neighbor_dict = find_neighbors(seats, nearest=True)
while changes > 0:
    seats, changes = step(seats, neighbor_dict, 4)
    steps += 1

print(sum([row.count(1) for row in seats]))


seats = original_seats
changes = 1
steps = 0
neighbor_dict = find_neighbors(seats, nearest=False)
while changes > 0:
    seats, changes = step(seats, neighbor_dict, 5)
    steps += 1

print(sum([row.count(1) for row in seats]))
