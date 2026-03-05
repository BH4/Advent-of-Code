

grid = []
with open('input4.txt', 'r') as f:
    for line in f:
        grid.append([x for x in line.strip()])


def neighbor_count(i, j):

    c = 0
    for ni in range(-1, 2):
        for nj in range(-1, 2):
            if not (ni == 0 and nj == 0):
                check = (i+ni, j+nj)
                if 0 <= check[0] < len(grid) and 0 <= check[1] < len(grid[0]):
                    if grid[check[0]][check[1]] == '@':
                        # print(check)
                        c += 1
    return c


tot_removed = 0
just_removed = None
while just_removed is None or just_removed > 0:
    to_remove = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '@':
                continue

            if neighbor_count(i, j) < 4:
                to_remove.append((i, j))

    if just_removed is None:
        print(len(to_remove))
    just_removed = len(to_remove)

    tot_removed += just_removed

    # removing
    for i, j in to_remove:
        grid[i][j] = '.'

print(tot_removed)
