from itertools import combinations


# Each machine has indicator light diagram, button wirings, joltage requirements
# ((lights), (buttons), (joltage))
# lights = tuple of indices for lights that should be on
# buttons = list of tuples of lights changed by each button
# joltage tuple of ints
machines = []
with open('input10.txt', 'r') as f:
    for line in f:
        line = line.strip()
        data = line.split(' ')

        lights_str = data[0]
        buttons_str = data[1:-1]
        joltage_str = data[-1]

        lights = []
        for ind, c in enumerate(lights_str[1:-1]):
            if c == '#':
                lights.append(ind)
        lights = tuple(lights)

        buttons = []
        for b in buttons_str:
            buttons.append(tuple(int(x) for x in b[1:-1].split(',')))

        joltage = tuple(int(x) for x in joltage_str[1:-1].split(','))

        machines.append((lights, buttons, joltage))

# print(len(machines))  # 197
# print(max([len(x[0]) for x in machines]))  # 9
# print(max([len(x[1]) for x in machines]))  # 13


def min_buttons(lights, buttons):
    """
    Each button will either be pressed or not. There is no reason yet to push a
    button multiple times. So the minimum button presses is <= len(buttons)

    There is at most 13 buttons and only 197 machines. Searching all button
    combinations is possible then. Searching first for 1 button then 2 and so
    on allows for early stopping though.

    Could think of the buttons being base 2 integers and xoring them
    """

    # If one button turns on the exact lights we need then we are done.
    if lights in buttons:
        return 1

    button_inds = list(range(len(buttons)))
    for n in range(2, len(buttons)):
        for inds in combinations(button_inds, n):
            curr = set()
            for i in inds:
                curr = curr.symmetric_difference(set(buttons[i]))

            if curr == set(lights):
                return n

    return len(buttons)


print(sum([min_buttons(x[0], x[1]) for x in machines]))

"""

def reject(remaining_joltage, step, curr_min):
    if step > curr_min:
        return True

    if min(remaining_joltage) < 0:
        return True

    return False


def accept(remaining_joltage):
    return sum(remaining_joltage) == 0


def backtracking(buttons, remaining_joltage, step, curr_min=10**5):
    if reject(remaining_joltage, step, curr_min):
        return curr_min

    if accept(remaining_joltage):
        return step

    print(remaining_joltage)

    # We test each button we might press
    # Only check buttons beyond the current one since order doesn't matter
    for button_ind in range(len(buttons)):
        max_presses = min([remaining_joltage[i] for i in buttons[button_ind]])
        for press_times in range(max_presses, 0, -1):
            # Remove this button press from the remaining joltage
            for ind in buttons[button_ind]:
                remaining_joltage[ind] -= press_times

            result = backtracking(buttons[button_ind+1:], remaining_joltage, step+press_times, curr_min)
            if result < curr_min:
                curr_min = result

            # Revert changes to joltage
            for ind in buttons[button_ind]:
                remaining_joltage[ind] += press_times

    return curr_min


def joltage_solver(buttons, joltage):
    len_buttons = [len(x) for x in buttons]
    len_buttons, buttons = zip(*sorted(zip(len_buttons, buttons), reverse=True))
    min_presses = backtracking(buttons, list(joltage), 0)
    return min_presses

print(len(machines))
tot = 0
for i in range(len(machines)):
    x = machines[i]
    p = joltage_solver(x[1], x[2])
    tot += p

    print(i, p)
print(tot)
"""

import numpy as np
from scipy import optimize


def joltage_solver(buttons, joltage):
    """
    (I thought of this before the backtracking, but I didn't know how to solve
    it over integers)
    Minimum presses for joltage.
    Convert buttons into matrix

    (1,2) (0,4) (1,3) (1,3,5)
    becomes
    M = [[0, 1, 0, 0],
         [1, 0, 1, 1],
         [1, 0, 0, 0],
         [0, 0, 1, 1],
         [0, 1, 0, 0],
         [0, 0, 0, 1]]

    M*x = joltage

    solve for x, but there are likely multiple solutions.
    """

    M = np.zeros((len(joltage), len(buttons)))  # [[0]*len(buttons) for x in range(len(joltage))]
    for i, b in enumerate(buttons):
        for j in b:
            M[j][i] = 1

    M = np.array(M)
    joltage = np.array(joltage)

    bounds = optimize.Bounds(lb=0)  # 0 <= x_i
    obj = np.ones(len(buttons), dtype=np.int32)
    integrality = np.full_like(obj, True)  # x_i are integers

    constraints = optimize.LinearConstraint(A=M, lb=joltage, ub=joltage)

    # Objective is all ones so we minimize the sum of the returned vector
    res = optimize.milp(c=obj, constraints=constraints, integrality=integrality, bounds=bounds)
    if res.success:
        return int(sum(res.x))
    return None


tot = 0
for i in range(len(machines)):
    x = machines[i]
    p = joltage_solver(x[1], x[2])
    tot += p

print(tot)