
with open('input/input1.txt') as f:
    num_increases = 0
    prev = 100000000
    for line in f:
        num = int(line)
        if prev < num:
            num_increases += 1
        prev = num

print(num_increases)


with open('input/input1.txt') as f:
    num_increases = 0
    prev = 10**10
    nums = [10**8, 10**8, 10**8]
    for line in f:
        num = int(line)
        nums = nums[1:]+[num]
        if prev < sum(nums):
            num_increases += 1
        prev = sum(nums)

print(num_increases)
