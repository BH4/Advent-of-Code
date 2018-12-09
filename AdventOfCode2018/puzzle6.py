"""
The problem asks for Manhattan distances. Very important.
I missed this multiple times.

For the first problem the key insight is that any region which contains a point
on the bounding box for all the coordinates will have an infinite area. This is
only true because we are using Manhattan distances.
"""

import numpy as np


def closest_point_index(check, point_list):
    """
    Return the index of the point in point_list which is closest by Manhattan
    distance to check.
    Returns None if two points are equal distance.
    """
    dist = abs(point_list[:, 0]-check[0]) + abs(point_list[:, 1]-check[1])
    m = min(dist)
    if np.count_nonzero(dist == m) == 1:
        c_ind = np.argmin(dist)
        return c_ind
    return None


xmin = 10**5
xmax = 0
ymin = 10**5
ymax = 0
coords = []
with open('input/input6.txt') as f:
    for line in f:
        # Parse x and y coordinates from line
        line = line.strip()
        line = line.split(', ')

        x = int(line[0])
        y = int(line[1])

        coords.append([x, y])

        # Update bounding box
        if x > xmax:
            xmax = x
        elif x < xmin:
            xmin = x

        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y


coords = np.array(coords)

infinite_area_points = set()
areas = [0]*len(coords)

for i in range(xmin, xmax+1):
    for j in range(ymin, ymax+1):
        point = [i, j]
        c_ind = closest_point_index(point, coords)
        if c_ind is not None:
            if i == xmin or i == xmax or j == ymin or j == ymax:
                infinite_area_points.add(c_ind)

            areas[c_ind] += 1

# remove points of infinite area from consideration
for i in infinite_area_points:
    areas[i] = 0
print("Largest finite area: {}".format(max(areas)))

"""
The second problem is straight forward. Just search each point in the bounding
box for points with total distance less than the given limit.
"""


def total_distance(check, point_list):
    """
    Return the sum of all Manhattan distances from check to each point in
    point_list.
    """
    dist = abs(point_list[:, 0]-check[0]) + abs(point_list[:, 1]-check[1])
    return sum(dist)


num_good_points = 0
limit = 10**4

for i in range(xmin, xmax+1):
    for j in range(ymin, ymax+1):
        point = [i, j]
        if total_distance(point, coords) < limit:
            num_good_points += 1


print("Number of points with total Manhattan distance less than {}: {}".format(limit, num_good_points))
