from functools import reduce

valid1 = 0
valid2 = 0

trees = []

with open('input/input3.txt') as f:
    for line in f:
        trees.append(line.strip())


values = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # dx, dy
for dx, dy in slopes:
    count = 0
    x = 0
    y = 0
    while y < len(trees)-1:
        x = (x+dx) % len(trees[0])
        y += dy
        if trees[y][x] == '#':
            count += 1
    values.append(count)

print('Puzzle 1:', values[1])
print('Puzzle 2:', reduce((lambda x, y: x * y), values))
