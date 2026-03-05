from intcode_computer import run
from itertools import permutations

with open('input/input7.txt', 'r') as f:
    line = f.readline()

code = [int(x) for x in line.split(',')]

best_val = -10000

for x in permutations([0, 1, 2, 3, 4], 5):
    curr_input = 0

    for i in x:
        copy = [x for x in code]
        curr, _, out = run(copy, [i, curr_input])
        curr_input = out[0]

    if curr_input > best_val:
        best_val = curr_input

print(best_val)


best_val = -10000

for x in permutations([5, 6, 7, 8, 9], 5):
    curr_input = 0
    amplifiers = []
    for i in range(5):
        copy = [x for x in code]
        amplifiers.append([copy, 0])

    done = False
    first_pass = True
    while not done:
        for i, phase in enumerate(x):
            if first_pass:
                input_list = [phase, curr_input]
            else:
                input_list = [curr_input]

            curr, _, out = run(amplifiers[i][0], input_list, curr=amplifiers[i][1])
            # amplifiers[i][0] is modified directly
            amplifiers[i][1] = curr
            curr_input = out[0]

        first_pass = False
        if curr == -1:
            done = True

    if curr_input > best_val:
        best_val = curr_input

print(best_val)
