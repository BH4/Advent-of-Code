
def get_next(vals):
    if set(vals) == set([0]):
        return 0

    diff = []
    for i in range(len(vals)-1):
        diff.append(vals[i+1]-vals[i])
    n = get_next(diff)
    return vals[-1]+n


def get_prev(vals):
    if set(vals) == set([0]):
        return 0

    diff = []
    for i in range(len(vals)-1):
        diff.append(vals[i+1]-vals[i])
    n = get_prev(diff)
    return vals[0]-n


with open('input/input9.txt') as f:
    tot = 0
    tot_p = 0
    for line in f:
        line = line.strip()
        vals = [int(x) for x in line.split()]

        tot += get_next(vals)
        tot_p += get_prev(vals)

print(tot)
print(tot_p)
