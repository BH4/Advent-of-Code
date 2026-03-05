with open('input/input2.txt') as f:
    loc = [0, 0]
    for line in f:
        if line[0] == 'f':
            loc[0] += int(line[8:])
        elif line[0] == 'u':
            loc[1] -= int(line[3:])
        elif line[0] == 'd':
            loc[1] += int(line[5:])

    print(loc[0]*loc[1])


with open('input/input2.txt') as f:
    loc = [0, 0]
    aim = 0
    for line in f:
        x = int(line.split()[1])
        if line[0] == 'f':
            loc[0] += x
            loc[1] += x*aim
        elif line[0] == 'u':
            aim -= x
        elif line[0] == 'd':
            aim += x

    print(loc[0]*loc[1])
