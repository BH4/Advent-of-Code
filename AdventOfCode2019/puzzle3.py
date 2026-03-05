
wire1_pos = set()
wire1_steps = dict()
wire2_pos = set()
wire2_steps = dict()

with open('input/input3.txt', 'r') as f:
    line1 = f.readline()
    #line1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    directions = line1.split(',')
    curr = (0, 0)
    steps = 0
    for d in directions:
        if d[0] == 'L':
            for i in range(int(d[1:])):
                curr = (curr[0]-1, curr[1])
                steps += 1
                wire1_pos.add(curr)
                if curr not in wire1_steps:
                    wire1_steps[curr] = steps
        elif d[0] == 'R':
            for i in range(int(d[1:])):
                curr = (curr[0]+1, curr[1])
                steps += 1
                wire1_pos.add(curr)
                if curr not in wire1_steps:
                    wire1_steps[curr] = steps
        elif d[0] == 'U':
            for i in range(int(d[1:])):
                curr = (curr[0], curr[1]-1)
                steps += 1
                wire1_pos.add(curr)
                if curr not in wire1_steps:
                    wire1_steps[curr] = steps
        elif d[0] == 'D':
            for i in range(int(d[1:])):
                curr = (curr[0], curr[1]+1)
                steps += 1
                wire1_pos.add(curr)
                if curr not in wire1_steps:
                    wire1_steps[curr] = steps

    line2 = f.readline()
    #line2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
    directions = line2.split(',')
    curr = (0, 0)
    steps = 0
    for d in directions:
        if d[0] == 'L':
            for i in range(int(d[1:])):
                curr = (curr[0]-1, curr[1])
                steps += 1
                wire2_pos.add(curr)
                if curr not in wire2_steps:
                    wire2_steps[curr] = steps
        elif d[0] == 'R':
            for i in range(int(d[1:])):
                curr = (curr[0]+1, curr[1])
                steps += 1
                wire2_pos.add(curr)
                if curr not in wire2_steps:
                    wire2_steps[curr] = steps
        elif d[0] == 'U':
            for i in range(int(d[1:])):
                curr = (curr[0], curr[1]-1)
                steps += 1
                wire2_pos.add(curr)
                if curr not in wire2_steps:
                    wire2_steps[curr] = steps
        elif d[0] == 'D':
            for i in range(int(d[1:])):
                curr = (curr[0], curr[1]+1)
                steps += 1
                wire2_pos.add(curr)
                if curr not in wire2_steps:
                    wire2_steps[curr] = steps

intersections = list(wire1_pos & wire2_pos)
dist = [abs(x[0])+abs(x[1]) for x in intersections]
z = sorted(zip(dist, intersections))
print(z[0][0])




# Part 2
step_sum = [wire1_steps[x]+wire2_steps[x] for x in intersections]
z = sorted(zip(step_sum, intersections))
print(z[0][0])
