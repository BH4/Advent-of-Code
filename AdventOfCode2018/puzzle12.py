"""
If we assume the ..... => . rule exists then we can model the
infinite, one dimensional row of pots by an array containing all the living
plants in which we always make sure to also contain at least 4 dead plants on
both the left and the right side. This is because we know no living plants can
begin existing any further than 2 pots over from the nearest living one.

Keeping 4 is for convenience of coding the solution.

Using a dictionary of the rules we can easily go through each combination of 5
pots to determine the new configuration of plants that are alive (next_state).

This by itself is sufficient for the first part, but the second part requires
something faster. I'm not sure if this is true for all inputs, but with my
initial input the state reached a constant string which didn't change and
only the offset was shifting. It can also be noted that this change to the
offset must be constant since the offset has no affect on the change in the
next_state function. From there it is easy to quickly determine what the offset
should be when the required number of generations has passed.
"""


def next_state(state, rules, offset):
    """
    Assumes that the farthest left 4 and right 4 are dead. Will also append and
    prepend dead pots to make sure that is still true when its done.
    """
    new = ''.join([rules[state[i-2:i+3]] for i in range(2, len(state)-2)])
    offset -= 2

    while new[:4] != '....':
        new = '.'+new
        offset += 1

    while new[-4:] != '....':
        new = new+'.'

    return new, offset


with open('input/input12.txt') as f:
    initial = f.readline()
    initial = initial.strip()
    _, _, initial = initial.split()

    f.readline()

    rules = dict()
    for line in f:
        line = line.strip()
        start, end = line.split(' => ')
        rules[start] = end


def alive_ind_sum(gens, state, offset):
    for i in range(gens):
        prev_state = state
        prev_offset = offset
        state, offset = next_state(state, rules, offset)

        if prev_state == state and prev_offset == offset:
            break

        if prev_state == state and prev_offset != offset:
            # offset must be changing by a constant amount
            offset += (offset - prev_offset)*(gens-1-i)
            break

    alive_inds = [x-offset for x in range(len(state)) if state[x] == '#']
    return sum(alive_inds)


initial_len = len(initial)
initial = '....' + initial + '....'
offset = 4


print(alive_ind_sum(20, initial, offset))
print(alive_ind_sum(5*10**10, initial, offset))
