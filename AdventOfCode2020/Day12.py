from collections import defaultdict


instructions = []
with open('input/input12.txt') as f:
    for line in f:
        line = line.strip()
        command = line[0]
        value = int(line[1:])
        instructions.append((command, value))


def follow(inst):
    pos = (0, 0)
    d = (1, 0)
    move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    turn = {'R': ((0, 1), (-1, 0)), 'L': ((0, -1), (1, 0))}
    for command, value in inst:
        if command in move:
            c = move[command]
            pos = (pos[0]+value*c[0], pos[1]+value*c[1])
        elif command in turn:
            c = turn[command]
            v = value//90
            while v > 0:
                d = (c[0][0]*d[0]+c[0][1]*d[1], c[1][0]*d[0]+c[1][1]*d[1])
                v -= 1
        elif command == 'F':
            pos = (pos[0]+value*d[0], pos[1]+value*d[1])
        else:
            print('missed some')
    return pos


def follow2(inst):
    waypoint = (10, 1)
    pos = (0, 0)
    move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    turn = {'R': ((0, 1), (-1, 0)), 'L': ((0, -1), (1, 0))}
    for command, value in inst:
        if command in move:
            c = move[command]
            waypoint = (waypoint[0]+value*c[0], waypoint[1]+value*c[1])
        elif command in turn:
            c = turn[command]
            v = value//90
            while v > 0:
                waypoint = (c[0][0]*waypoint[0]+c[0][1]*waypoint[1], c[1][0]*waypoint[0]+c[1][1]*waypoint[1])
                v -= 1
        elif command == 'F':
            pos = (pos[0]+value*waypoint[0], pos[1]+value*waypoint[1])
        else:
            print('missed some')
    return pos


print(sum([abs(x) for x in follow(instructions)]))
print(sum([abs(x) for x in follow2(instructions)]))
