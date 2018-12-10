"""
This problem is most easily solved by looking for a property in the set of
points that should be minimized or maximized once the letters have formed.
Here I check the maximum number of vertical points at any time and assume
that when they are at a maximum the letters have formed.

It is possible that this method might not work for a different set of letters.
In that case it may be better to try something like minimizing the total
distance between points.

Plotting the points in a scatter plot is just the fastest way to see it.
Anything else would be much more complicated.

The second part can be easily solved by just keeping track of the amount
of time that has passed.
"""


from collections import defaultdict
from matplotlib import pyplot as plt


def propogate(points):
    """
    Advance every point by one time step.
    """
    new_points = []
    for p in points:
        new_pos = [p[0][0]+p[1][0], p[0][1]+p[1][1]]
        new_points.append([new_pos, p[1]])

    return new_points


def max_vert(points):
    """
    Return the maximum number of vertical points for any value of x at this
    point in time.
    """
    xvals = defaultdict(int)
    for p in points:
        xvals[p[0][0]] += 1

    return max(xvals.values())


def show(points):
    """
    Use a scatter plot to show what is hopefully the solution to part 1.
    """
    x = []
    y = []
    for p in points:
        x.append(p[0][0])
        # Need to flip the y values since the points are given such that
        # positive y is down.
        y.append(-1*p[0][1])

    plt.scatter(x, y)
    plt.show()


points = []
with open('input/input10.txt') as f:
    for line in f:
        to_replace = ['<', '>', ',']
        for r in to_replace:
            line = line.replace(r, ' ')

        line = line.split()
        pos = [int(line[1]), int(line[2])]
        vel = [int(line[4]), int(line[5])]
        points.append([pos, vel])


most_vert = 0
best = []
time = 0
for i in range(11000):
    curr = max_vert(points)
    if curr >= most_vert:
        most_vert = curr
        time = i
        best = points
    points = propogate(points)

show(best)
print("Time taken to get letters: {} seconds".format(time))
