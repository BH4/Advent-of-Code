import re

def split_to_stacks(line):
    i = 1
    elems = []
    while i < len(line):
        curr = line[i]
        if curr != ' ':
            elems.append([curr])
        else:
            elems.append([])
        i += 4

    return elems


def move(stacks, num, start, end, reverse=True):
    moved = stacks[start][:num]
    stacks[start] = stacks[start][num:]
    if reverse:
        stacks[end] = moved[::-1]+stacks[end]
    else:
        stacks[end] = moved+stacks[end]
    return stacks


part1 = False  # False is part 2

stacks_done = False
format_string = 'move (.*) from (.*) to (.*)'
with open('input5.txt') as f:
    stacks = [[] for x in range(9)]  # first index is the top of the stack
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue

        if not stacks_done and line[0] == '1':
            stacks_done = True

        if not stacks_done:
            for i, e in enumerate(split_to_stacks(line)):
                stacks[i] += e

        if stacks_done and line[0] == 'm':
            num, start, end = [int(x) for x in re.findall(format_string, line)[0]]
            stacks = move(stacks, num, start-1, end-1, reverse=part1)


s = ''
for x in stacks:
    if len(x) > 0:
        s += x[0]
print(s)
