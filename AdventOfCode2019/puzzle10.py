from collections import defaultdict

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def reduced_form(f):
    n, d = f
    assert n != 0 or d != 0

    if n == 0:
        return (0, d//abs(d))

    if d == 0:
        return (n//abs(n), 0)

    g = gcd(abs(n), abs(d))
    return (n//g, d//g)


astroids = []

with open('input/input10.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line):
            if c == '#':
                astroids.append((x, y))

largest_num = 0
best_pos = ()
best_dict = defaultdict(list)
for i in range(len(astroids)):
    a1 = astroids[i]
    visible_slopes = set()
    astroids_with_slope = defaultdict(list)  # later sort by distance from a1
    for j in range(len(astroids)):
        if i != j:
            a2 = astroids[j]
            slope = (a2[1]-a1[1], a2[0]-a1[0])
            distance = (a2[1]-a1[1])**2 + (a2[0]-a1[0])**2
            rf = reduced_form(slope)
            visible_slopes.add(rf)
            astroids_with_slope[rf].append((distance, a2))

    vis = len(visible_slopes)
    if vis > largest_num:
        largest_num = vis
        best_pos = a1
        best_dict = astroids_with_slope

print(largest_num)


# sort best_dict keys into clockwise order starting with up then sort each
# value list of best_dict by the distance value

slopes = best_dict.keys()
sort_val = []
for x in slopes:
    if x[1] == 0:
        sort_val.append((0, 10000000*x[0]/abs(x[0])))
    elif x[1] > 0:
        sort_val.append((0, x[0]/x[1]))
    elif x[1] < 0:
        sort_val.append((1, x[0]/x[1]))


z = sorted(zip(sort_val, slopes))
sort_val, slopes = zip(*z)

for x in slopes:
    best_dict[x] = sorted(best_dict[x])

count = 0
s_ind = 0
while count < 200:
    astroid = best_dict[slopes[s_ind]].pop(0)

    s_ind = (s_ind+1) % len(slopes)
    count += 1

print(astroid[1][0]*100+astroid[1][1])
