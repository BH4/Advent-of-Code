"""
Input:
<x=1, y=3, z=-11>
<x=17, y=-10, z=-8>
<x=-1, y=-15, z=2>
<x=12, y=-4, z=-4>
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def step(pos, vel):

    for i in range(len(pos)-1):
        for j in range(i+1, len(pos)):
            for coord in range(3):
                if pos[i][coord] > pos[j][coord]:
                    vel[i][coord] -= 1
                    vel[j][coord] += 1
                elif pos[i][coord] < pos[j][coord]:
                    vel[i][coord] += 1
                    vel[j][coord] -= 1

    for i in range(len(pos)):
        for coord in range(3):
            pos[i][coord] += vel[i][coord]

    return pos, vel


def energy(pos, vel):
    tot = 0
    for i in range(len(pos)):
        potential = 0
        for c in pos[i]:
            potential += abs(c)

        kinetic = 0
        for c in vel[i]:
            kinetic += abs(c)

        tot += potential*kinetic

    return tot


pos = [[1, 3, -11], [17, -10, -8], [-1, -15, 2], [12, -4, -4]]
vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for steps in range(1000):
    pos, vel = step(pos, vel)

print(energy(pos, vel))


# Part 2  Figures out how to determine the period of repeats for just one dimension. then it should be easy to solve.

coord_steps = []
for coord in range(3):
    pos = [[1, 3, -11], [17, -10, -8], [-1, -15, 2], [12, -4, -4]]
    vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    prev = set()
    state = (str([m[coord] for m in pos]), str([m[coord] for m in vel]))
    prev.add(state)

    steps = 0
    done = False
    while not done:
        pos, vel = step(pos, vel)
        steps += 1

        state = (str([m[coord] for m in pos]), str([m[coord] for m in vel]))

        if state in prev:
            done = True
        else:
            prev.add(state)

    coord_steps.append(steps)

print(lcm(lcm(coord_steps[0], coord_steps[1]), coord_steps[2]))
