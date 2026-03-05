
def anyone_yes_count(group):
    s = set()
    for g in group:
        s |= set(g)
    return len(s)

def everyone_yes_count(group):
    s = set(group[0])
    for g in group:
        s &= set(g)
    return len(s)


groups = []

with open('input/input6.txt') as f:
    group = []
    for line in f:
        if len(line.strip()) == 0:
            groups.append(group)
            group = []
        else:
            group.append(line.strip())

    if len(group) != 0:
        groups.append(group)


tot = 0
for g in groups:
    v = anyone_yes_count(g)
    tot += v
print(tot)

tot = 0
for g in groups:
    v = everyone_yes_count(g)
    tot += v
print(tot)
