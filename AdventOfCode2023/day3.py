from collections import defaultdict


with open('input/input3.txt') as f:
    M = []
    for line in f:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)

        M.append(row)


gear_parts = defaultdict(list)


def is_symbol(j, i, num):
    if i < 0 or j < 0 or i >= len(M) or j >= len(M[0]):
        return False

    s = M[i][j]
    if s.isdigit():
        print('uhhh undefined?')
        return False
    if s == '.':
        return False

    if s == '*':
        gear_parts[(i, j)].append(num)

    return True


def is_part_num(start, end, row_ind, num):
    # Loop over one more than the numbers size on each side
    # above and below.
    check = False
    for j in range(start-1, end+2):
        if is_symbol(j, row_ind-1, num):
            check = True

        if is_symbol(j, row_ind+1, num):
            check = True

    # Check end caps as well
    if is_symbol(start-1, row_ind, num) or is_symbol(end+1, row_ind, num):
        check = True

    return check


# Go through left to right and find all numbers then check surroundings for symbols
part_sum = 0
for i, row in enumerate(M):
    reading = False
    curr = 0
    start = None
    for j, c in enumerate(row):
        if c.isdigit():
            if not reading:
                start = j
            reading = True
            curr = curr*10+int(c)
        elif reading:
            if is_part_num(start, j-1, i, curr):
                part_sum += curr

            reading = False
            curr = 0
            start = None

    if reading:
        if is_part_num(start, j, i, curr):
            part_sum += curr

print(part_sum)


gear_sum = 0
for g_ind, part_list in gear_parts.items():
    if len(part_list) == 2:
        gear_sum += part_list[0]*part_list[1]

print(gear_sum)
