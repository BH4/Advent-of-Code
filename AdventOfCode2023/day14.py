f = open('input/input14.txt')
dish = f.read().strip().split('\n')
dish = [[x for x in y] for y in dish]
f.close()


def load(dish):
    tot = 0
    for i in range(len(dish)):
        for j in range(len(dish[0])):
            if dish[i][j] == 'O':
                tot += len(dish)-i
    return tot


def roll(dish):
    for i in range(len(dish)):
        for j in range(len(dish[0])):
            if dish[i][j] == 'O':
                stop = i-1
                while stop >= 0 and dish[stop][j] == '.':
                    stop -= 1

                if not(stop+1 == i or (dish[stop+1][j] == '.' and (stop < 0 or dish[stop][j] != '.'))):
                    print(dish[stop+1][j], stop, dish[stop][j])
                    print()
                    quit()

                if stop+1 != i:
                    dish[stop+1][j] = 'O'
                    dish[i][j] = '.'
    return dish


def rot(dish):
    """
    Rotate dish 90 right so that north becomes east
    """

    return [[dish[i][j] for i in range(len(dish)-1, -1, -1)] for j in range(len(dish[0]))]


def cycle(dish):
    for i in range(4):
        dish = rot(roll(dish))
    return dish


# print(load(roll(dish)))

print(load(dish))
sofar = 0
for i in range(150):  # Originally used larger number to get to cycle
    dish = cycle(dish)
    sofar += 1

pattern = [load(dish)]
dish = cycle(dish)
sofar += 1
L = load(dish)
pattern.append(L)
while L != pattern[0]:
    dish = cycle(dish)
    sofar += 1
    L = load(dish)
    pattern.append(L)

pattern = pattern[:-1]

# Works because sofar corresponds to pattern[0]
print(pattern[(1000000000-sofar) % len(pattern)])
