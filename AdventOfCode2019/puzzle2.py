from intcode_computer import run

"""
def run(code):
    curr = 0
    while code[curr] != 99:
        in_ind1 = code[curr+1]
        in_ind2 = code[curr+2]
        out_ind = code[curr+3]

        if code[curr] == 1:
            code[out_ind] = code[in_ind1]+code[in_ind2]
        elif code[curr] == 2:
            code[out_ind] = code[in_ind1]*code[in_ind2]
        else:
            print('error')
            quit()

        #print(in_ind1, in_ind2, out_ind, code)

        curr += 4

    return code
"""

with open('input/input2.txt', 'r') as f:
    line = f.readline()

code = [int(x) for x in line.split(',')]

# Part 1 -----------------------------------------------------
# Replace replace position 1 with the value 12 and
# replace position 2 with the value 2 before running.

copy = [x for x in code]
copy[1] = 12
copy[2] = 2
_, copy, _ = run(copy, [])
print(copy[0])


# Part 2 -----------------------------------------------------

for a in range(100):
    for b in range(100):
        copy = [x for x in code]
        copy[1] = a
        copy[2] = b
        _, copy, _ = run(copy, [])
        if copy[0] == 19690720:
            print(100*a+b)
