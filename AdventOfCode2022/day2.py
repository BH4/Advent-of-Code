score = 0

with open('input2.txt') as f:
    for line in f:
        line = line.strip()
        them, me = line.split(' ')
        score += ord(me)-ord('X')+1

        if them == 'A':  # rock
            if me == 'X':
                score += 3
            if me == 'Y':
                score += 6
            if me == 'Z':
                score += 0
        elif them == 'B':  # paper
            if me == 'X':
                score += 0
            if me == 'Y':
                score += 3
            if me == 'Z':
                score += 6
        elif them == 'C':  # scissors
            if me == 'X':
                score += 6
            if me == 'Y':
                score += 0
            if me == 'Z':
                score += 3

print(score)

score = 0

with open('input2.txt') as f:
    for line in f:
        line = line.strip()
        them, me = line.split(' ')
        score += (ord(me)-ord('X'))*3

        if them == 'A':  # rock
            if me == 'X':
                score += 3
            if me == 'Y':
                score += 1
            if me == 'Z':
                score += 2
        elif them == 'B':  # paper
            if me == 'X':
                score += 1
            if me == 'Y':
                score += 2
            if me == 'Z':
                score += 3
        elif them == 'C':  # scissors
            if me == 'X':
                score += 2
            if me == 'Y':
                score += 3
            if me == 'Z':
                score += 1

print(score)
