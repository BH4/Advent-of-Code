"""
Basic brute force solution. Just loop over all possible starting points and sum
all the numbers in the nxn square. For the first part just check 3x3 and for
the second part check all n from 1 to 300.

Solution to part 2 takes about 90 seconds.
"""


import numpy as np

grid_num = 7803
# grid_num = 18
side_len = 300


def fuel_level(x, y):
    rack_id = x+10
    power = rack_id*y
    power += grid_num
    power = power*rack_id
    power = (power//100) % 10
    power -= 5

    return power


def get_grid():
    grid = []
    for x in range(1, side_len+1):
        row = []
        for y in range(1, side_len+1):
            row.append(fuel_level(x, y))
        grid.append(row)

    return np.array(grid)


def best_square_n(grid, n):
    best = ()
    best_power = 0
    for x in range(side_len-n+1):
        for y in range(side_len-n+1):
            square = grid[x:x+n, y:y+n].sum()

            if square > best_power:
                best_power = square
                best = (x+1, y+1)

    return best, best_power


grid = get_grid()
print(best_square_n(grid, 3)[0])

"""
Solution to part 2 takes about 90 seconds. Need to think of a faster way.
"""

ans = ()
ans_power = 0
for n in range(1, 300):
    check, check_power = best_square_n(grid, n)
    if check_power > ans_power:
        ans_power = check_power
        ans = (check[0], check[1], n)

print(ans)
