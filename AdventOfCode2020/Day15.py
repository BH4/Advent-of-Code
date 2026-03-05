start = [2, 0, 6, 12, 1, 3]

last_ind = dict()
last_num = start[-1]
curr_ind = len(start)
for i, x in enumerate(start[:-1]):
    last_ind[x] = i

while curr_ind < 30000000:
    if last_num in last_ind:
        next_num = (curr_ind-1)-last_ind[last_num]
    else:
        next_num = 0

    last_ind[last_num] = curr_ind-1
    last_num = next_num
    curr_ind += 1

    if curr_ind == 2020:
        print(last_num)

print(last_num)
