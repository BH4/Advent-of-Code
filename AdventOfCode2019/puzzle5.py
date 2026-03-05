from intcode_computer import run

with open('input/input5.txt', 'r') as f:
    line = f.readline()

code = [int(x) for x in line.split(',')]
copy = [x for x in code]

stdin = [1]
_, _, out = run(copy, stdin)
print(out[-1])

copy = [x for x in code]
stdin = [5]
_, _, out = run(copy, stdin)
print(out[0])
