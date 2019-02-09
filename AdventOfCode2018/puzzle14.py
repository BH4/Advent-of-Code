from copy import deepcopy

def step(state):
    recipes, elf1, elf2 = state

    new_r = recipes[elf1]+recipes[elf2]
    recipes += [int(x) for x in str(new_r)]

    elf1 = (elf1+recipes[elf1]+1) % len(recipes)
    elf2 = (elf2+recipes[elf2]+1) % len(recipes)

    return [recipes, elf1, elf2]


def part1(after, state):
    state = deepcopy(state)
    while len(state[0]) < 10+after:
        state = step(state)

    return ''.join([str(x) for x in state[0][after:after+10]])


def part2(find, state):
    state = deepcopy(state)
    while len(state[0]) < len(find):
        state = step(state)

    # While find has not been created yet keep stepping forward
    test1 = ''.join([str(x) for x in state[0][-len(find):]])
    test2 = ''.join([str(x) for x in state[0][-len(find)-1:-1]])
    while test1 != find and test2 != find:
        state = step(state)
        test1 = ''.join([str(x) for x in state[0][-len(find):]])
        test2 = ''.join([str(x) for x in state[0][-len(find)-1:-1]])

    if test2 == find:
        return len(state[0])-len(find)-1
    return len(state[0])-len(find)


puzzle_input = '635041'
recipes = [int(x) for x in '37']

state = [recipes, 0, 1]

print(part1(puzzle_input, state))
print(part2(str(puzzle_input), state))
