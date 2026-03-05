"""
My recursive function wasnt written with reducing the input as much as possible
in mind and on trying to reduce it I assumed the input product was valid.

Need to redo from scratch with idea of reducing input as much as possible so I
can memorize small strings answers.
"""






def memo(func):
    mem = dict()

    def helper(*args):
        if args not in mem:
            mem[args] = func(*args)

        return mem[args]
    return helper


f = open('input/input12.txt')
lines = f.read().strip().split('\n')
f.close()

sym = []
nums = []
for line in lines:
    s, n = line.split(' ')
    sym.append(s)
    nums.append(tuple(int(x) for x in n.split(',')))


verbose = False
def my_print(*args):
    if verbose:
        print(*args)


@memo
def num_ways(check, sol, started):
    """
    started => previously removed some # that hasn't terminated at a '.'
    """
    my_print(check, sol, started)

    if check.count('#') > sum(sol):
        return 0

    if (check == '.' or check == '') and sol == (0,):
        return 1

    if len(check) == 0:
        return 0

    if len(sol) == 0:
        my_print('empty sol')
        if check == '#':
            return 0
        return 1

    if check[0] == '.':
        my_print('has .')
        if started and sol[0] != 0:
            my_print('died because not enough # in a row')
            return 0

        if started:
            return num_ways(check[1:], sol[1:], False)
        return num_ways(check[1:], sol, False)

    if check[0] == '#':
        my_print('has #')
        if sol[0] == 0:
            my_print('Died because too many # in a row')
            return 0
        sol = list(sol)
        return num_ways(check[1:], tuple([sol[0]-1]+sol[1:]), True)

    my_print('has ?')
    # check[0] == '?'
    a = num_ways('.'+check[1:], sol, started)
    b = num_ways('#'+check[1:], sol, started)
    # print(check, sol, started)
    # print(a, b)
    return a+b


tot = 0
for i in range(len(sym)):
    p = num_ways(sym[i], nums[i], False)
    tot += p
    # print(sym[i], nums[i], p)

print(tot)

tot = 0
for i in range(len(sym)):
    s = '?'.join([sym[i], sym[i], sym[i], sym[i], sym[i]])
    n = nums[i]*5
    p = num_ways(s, n, False)
    tot += p
    # print(sym[i], nums[i], p)

print(tot)