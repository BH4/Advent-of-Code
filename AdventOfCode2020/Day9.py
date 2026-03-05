
nums = []
with open('input/input9.txt') as f:
    for line in f:
        nums.append(int(line.strip()))


def prev_sums(nums):
    sums = set()
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            sums.add(nums[i]+nums[j])
    return sums


ind = 25
sums = prev_sums(nums[:ind])
while nums[ind] in sums:
    ind += 1
    sums = prev_sums(nums[ind-25:ind])

val = nums[ind]
print(val)

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if sum(nums[i:j+1]) == val:
            print(min(nums[i:j+1])+max(nums[i:j+1]))
            quit()
