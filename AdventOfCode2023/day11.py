import numpy as np
from bisect import bisect


empty_row = []

U = []
with open('input/input11.txt') as f:
    ind = 0
    for line in f:
        line = line.strip()
        row = [x for x in line]
        if '#' not in row:
            # U.append(['.']*len(row))
            empty_row.append(ind)
        U.append(row)

        ind += 1

# expand columns
U = np.array(U)
empty_column = []
for ind in range(len(U[0])):
    if '#' not in U[:, ind]:
        empty_column.append(ind)

# empty = empty[::-1]
# for e in empty:
#     U = np.insert(U, e, '.', axis=1)


G = list(zip(*np.where(U == '#')))


expansion = [2, 1000000]
for exp in expansion:
    dist = 0
    for i in range(len(G)-1):
        for j in range(i+1, len(G)):
            dist += abs(G[i][0]-G[j][0])+abs(G[i][1]-G[j][1])

            # add expansion distance
            a = bisect(empty_row, G[i][0])
            b = bisect(empty_row, G[j][0])
            c = bisect(empty_column, G[i][1])
            d = bisect(empty_column, G[j][1])
            num_empty = abs(a-b)+abs(c-d)
            dist += (exp-1)*num_empty

    print(dist)
