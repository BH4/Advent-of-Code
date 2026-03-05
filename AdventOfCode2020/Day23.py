
def move_fast(cups, curr, m):
    # Preforms one move operation
    # cups[c] = cup clockwise from cup c

    # remove 3 cups after current cup
    removed = [cups[curr]]
    for i in range(2):
        removed.append(cups[removed[-1]])

    cups[curr] = cups[removed[-1]]

    # Find destination cup
    dest = curr-1
    if dest == 0:
        dest = m
    while dest in removed:
        dest = dest-1
        if dest == 0:
            dest = m

    # Put cups clockwise from destination
    temp = cups[dest]
    cups[dest] = removed[0]
    cups[removed[2]] = temp

    # Return new cup order and new current cup
    return cups, cups[curr]


if __name__ == '__main__':
    cups_str = '653427918'

    cups_arr = [int(x) for x in cups_str]
    curr = cups_arr[0]
    m = max(cups_arr)
    cups = [0]*(m+1)
    for i in range(len(cups_arr)):
        cups[cups_arr[i]] = cups_arr[(i+1) % len(cups_arr)]

    for j in range(100):
        cups, curr = move_fast(cups, curr, m)

    ans = [cups[1]]
    while cups[ans[-1]] != 1:
        ans.append(cups[ans[-1]])
    print(''.join([str(x) for x in ans]))

    cups_str = '653427918'

    cups_arr = [int(x) for x in cups_str]
    m = max(cups_arr)
    curr = cups_arr[0]
    cups_arr = cups_arr + list(range(m+1, 1000000+1))
    m = 1000000
    cups = [0]*(m+1)
    for i in range(len(cups_arr)):
        cups[cups_arr[i]] = cups_arr[(i+1) % len(cups_arr)]

    for j in range(10000000):
        cups, curr = move_fast(cups, curr, m)

    ans = [cups[1], cups[cups[1]]]
    print(ans[0]*ans[1])
