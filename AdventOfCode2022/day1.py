
elves = []

with open('input1.txt', 'r') as f:
    curr_elf = []
    for line in f:
        line = line.strip()
        if len(line) == 0:
            elves.append(sum(curr_elf))
            curr_elf = []
        else:
            curr_elf.append(int(line))

elves = sorted(elves)
print(elves[-1])
print(sum(elves[-3:]))
