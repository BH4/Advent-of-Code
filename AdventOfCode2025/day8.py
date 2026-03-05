import numpy as np


class disjointSets:
    def __init__(self, n):
        self.sets = [-1]*n
        self.size = n

    # returns true or false as to weather or not a union was preformed
    def union(self, a, b):  # union by size
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # union was not preformed

        newSize = self.sets[rootA]+self.sets[rootB]#size is negative the number of elements of the set

        # rootA has more elements
        if self.sets[rootA] < self.sets[rootB]:
            self.sets[rootB] = rootA
            self.sets[rootA] = newSize
        else:  # B has more or same
            self.sets[rootA] = rootB
            self.sets[rootB] = newSize

        self.size -= 1

        return True  # union was preformed

    def find(self, a):  # finds root of element with id 'a'
        # also make the parents of this node the root in order to decrease tree height

        parent = self.sets[a]
        if parent < 0:
            return a

        root = self.find(parent)

        self.sets[a] = root

        return root


def dist(v1, v2):
    diff2 = [(v1[i]-v2[i])**2 for i in range(3)]
    return np.sqrt(sum(diff2))


# location and circuit index
boxes = []
count = 0
with open('input8.txt', 'r') as f:
    for line in f:
        line = line.strip()

        coords = tuple(int(x) for x in line.split(','))
        boxes.append(coords)


# Get 1000 smallest distances
pair_dist = []
for i in range(len(boxes)-1):
    for j in range(i+1, len(boxes)):
        d = dist(boxes[i], boxes[j])
        pair_dist.append((d, i, j))

pair_dist.sort()

# Merge boxes and count using disjoint sets
ds = disjointSets(len(boxes))
for i in range(1000):
    ds.union(pair_dist[i][1], pair_dist[i][2])

v = sorted(ds.sets)
print(v[0]*v[1]*v[2]*-1)

# continue combining
last_prod = None
curr = 1000
while ds.size > 1:
    i = pair_dist[curr][1]
    j = pair_dist[curr][2]
    last_prod = boxes[i][0]*boxes[j][0]
    ds.union(i, j)
    curr += 1

print(last_prod)
