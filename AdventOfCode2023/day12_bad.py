f = open('input/input12.txt')
lines = f.read().strip().split('\n')
f.close()

sym = []
nums = []
for line in lines:
    s, n = line.split(' ')
    sym.append(s)
    nums.append(tuple(int(x) for x in n.split(',')))


def count(check):
    counts = []
    curr = 0
    on = False
    for s in check:
        if s == '#':
            curr += 1
            on = True
        elif on:
            on = False
            counts.append(curr)
            curr = 0

    if curr > 0:
        counts.append(curr)
    return tuple(counts)


def accept(check, sol):
    return count(check) == sol


def reject(check, sol):
    c = count(check)
    q = check.count('?')
    if q == 0:
        # print('not accepted and no more ?')
        return True

    if sum(c) + q < sum(sol):
        # print(c, sum(c), q, sum(sol), check)
        # print('not enough room to add #')
        return True

    # if len(c) > 0 and c[0] > sol[0]:
    #     print('too many #. oops this can be wrong')
    #     return True

    if sum(c) > sum(sol):
        # print('too many #')
        return True

    return False


def possible_ways(check, sol):
    # print(check, sol)
    if accept(check, sol):
        # print('accept')
        return 1
    if reject(check, sol):
        # print('reject')
        return 0

    ind = check.index('?')
    ways = 0
    for c in ['.', '#']:
        new_check = check[:ind]+c+check[ind+1:]
        ways += possible_ways(new_check, sol)

    return ways


# print(possible_ways('?#?#?#?#?#?#?#?', (1,3,1,6)))
# quit()


tot = 0
for i in range(len(sym)):
    p = possible_ways(sym[i], nums[i])
    tot += p
    print(sym[i], nums[i], p)

print(tot)
