from collections import defaultdict

nums = []
with open('input/input10.txt') as f:
    for line in f:
        nums.append(int(line.strip()))

nums = sorted(nums)
nums.append(nums[-1]+3)
nums = [0]+nums


diffs = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
ones = diffs.count(1)
threes = diffs.count(3)
print(ones*threes)

# Count numbers that are not part of a difference of 3.
# They are all either 3 or 1 away in my version.
not_part_of_3_diff = [1]*len(nums)
prev = 0
for i in range(1, len(nums)):
    n = nums[i]
    if n-prev == 3:
        not_part_of_3_diff[i-1] = 0
        not_part_of_3_diff[i] = 0

    prev = n

"""
Adapters that are 3 away from either neighbor must be used.
Denote these adapters by 0 (this includes the charging outlet since it must be
used) and others by 1. We are interested in the adapters that can be excluded.
This can only happen in patterns like
010
0110
01110
ect.
The 1s between the zeros can be removed. In the 010 case this
results in 2 distinct arrangements. 0110 has 4. 01110 cannot remove
all three of the 1s so it has 7 arrangements.
Further patterns can be explored, but my example doesn't need it.
Multiplying the number of arrangements for each sub-pattern gives
the total number of arrangements.
"""

tot = 1
count = 0
for i in not_part_of_3_diff[1:]:
    if i == 1:
        count += 1
    else:
        if count > 0:
            if count == 1:
                tot *= 2
            elif count == 2:
                tot *= 4
            elif count == 3:
                tot *= 7
            else:
                print('Missed some.')

            count = 0

print(tot)
