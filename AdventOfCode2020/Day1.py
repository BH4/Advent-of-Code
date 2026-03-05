nums = []

with open('input/input1a.txt') as f:
    for line in f:
        nums.append(int(line.strip()))


puzzle1 = 0
puzzle2 = 0


for i in range(len(nums)-2):
    x = nums[i]
    for j in range(i, len(nums)-1):
        y = nums[j]
        if x+y == 2020:
            puzzle1 = x*y

        if x+y < 2020:
            for k in range(j, len(nums)):
                z = nums[k]
                if x+y+z == 2020:
                    puzzle2 = x*y*z

print('Puzzle 1:', puzzle1)
print('Puzzle 2:', puzzle2)
