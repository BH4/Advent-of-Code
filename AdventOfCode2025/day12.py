"""
It's certainly a constraint satisfaction problem
I will try backtracking. Tests will be adding a shape at each point and all 8
rotations and flips. Each shape is 3x3 so use the center point as the point I
add the shape. This also means that the boarders and corners will not fit any
shape.

Issue is there are too many places to check... recursion limit and takes too long
Maybe instead I should build dense squares by hand or something? That might
work...
"""
import numpy as np


shapes = []
regions = []
with open('input12.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0 and line[-1] == ':':
            s = [[1 if x == '#' else 0 for x in f.readline().strip()]]
            s.append([1 if x == '#' else 0 for x in f.readline().strip()])
            s.append([1 if x == '#' else 0 for x in f.readline().strip()])

            shapes.append(s)
        elif ':' in line:
            w_h, counts = line.split(': ')
            w, h = [int(x) for x in w_h.split('x')]
            counts = [int(x) for x in counts.split(' ')]

            regions.append((w, h, counts))


def trivial_check(w, h, counts):
    areas = [5, 7, 6, 7, 7, 7]
    c = sum(counts)
    if (w//3)*(h//3) >= c:
        return True, True  # Trivial, possible

    tot = 0
    for i, ci in enumerate(counts):
        tot += areas[i]*ci
    if tot > w*h:
        return True, False  # Trivial, not possible

    return False, None


tot = 0
tot_triv = 0
solved = 0
for y in regions:
    t, sol = trivial_check(*y)
    if t:
        tot_triv += 1
    if sol:
        solved += 1
    tot += 1
print(solved)
print(tot_triv)
print(tot)
quit()



# Convert shapes to numpy arrays and list all of their rotations together.
# Shapes must keep the same ordering.
for ind, s in enumerate(shapes):
    shape_rots_flips = []
    seen = set()
    s = np.array(s)

    for _ in range(4):  # rotations
        # Not flipped
        s_hash = s.tobytes()
        if s_hash not in seen:
            shape_rots_flips.append(s)
            seen.add(s_hash)

        # Flipped
        sf = np.flip(s, axis=0)
        sf_hash = sf.tobytes()
        if sf_hash not in seen:
            shape_rots_flips.append(sf)
            seen.add(sf_hash)

        # Rotate for next iteration
        s = np.rot90(s)

    shapes[ind] = shape_rots_flips


shape_test_order = []
for shape_ind, all_rot in enumerate(shapes):
    for rot_ind, s in enumerate(all_rot):
        shape_test_order.append((shape_ind, rot_ind))


def reject(region, counts, last_loc):
    if min(counts) < 0:
        return True

    if last_loc is None:
        return False

    for i in range(3):
        for j in range(3):
            if region[last_loc[0]+i-1][last_loc[1]+j-1] > 1:
                return True

    return False


def accept(region, counts):
    return sum(counts) == 0


def add_shape(region, s, loc):
    # In place changes!
    for i in range(3):
        for j in range(3):
            region[loc[0]+i-1][loc[1]+j-1] += s[i][j]


def backtracking(curr_region, remaining_counts, curr_location, prev_location):
    # print(curr_region)
    if reject(curr_region, remaining_counts, prev_location):
        return False

    if accept(curr_region, remaining_counts):
        return True

    # Check curr location is viable, else reject
    valid = (1 <= curr_location[0] <= len(curr_region)-2 and 1 <= curr_location[1] <= len(curr_region[0])-2)
    if not valid:
        return False

    # We test each shape in the shape_test_order at the current location and
    # leave it empty if none work.
    next_location = (curr_location[0], curr_location[1]+1)
    if next_location[1] > len(curr_region[0])-2:
        next_location = (curr_location[0]+1, 1)

    # print(next_location)

    for shape_ind in shape_test_order:
        curr_s = shapes[shape_ind[0]][shape_ind[1]]

        # Get the test region and test remaining_counts
        remaining_counts[shape_ind[0]] -= 1
        add_shape(curr_region, curr_s, curr_location)

        result = backtracking(curr_region, remaining_counts, next_location, curr_location)
        if result:
            return result

        # Revert changes to counts and region
        remaining_counts[shape_ind[0]] += 1
        add_shape(curr_region, -1*curr_s, curr_location)

    # Finally test skipping this location
    result = backtracking(curr_region, remaining_counts, next_location, None)
    if result:
        return result

    return False


def initiate_backtracking(w, h, counts):
    initial_region = np.zeros((h, w))

    remaining_counts = counts
    curr_location = (1, 1)

    can_fit = backtracking(initial_region, remaining_counts, curr_location, None)
    return can_fit


print(initiate_backtracking(*regions[0]))
