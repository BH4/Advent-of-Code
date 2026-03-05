from collections import defaultdict


with open('input/input5.txt') as f:
    seeds = f.readline()
    seeds = [int(x) for x in seeds.split(':')[1].strip().split()]
    f.readline()
    f.readline()

    maps = []
    curr_dict = dict()
    for line in f:
        line = line.strip()
        if len(line) > 0:
            a, b, c = [int(x) for x in line.split()]
            curr_dict[b] = (c, a)
        else:
            maps.append(curr_dict)
            curr_dict = dict()
            f.readline()

    maps.append(curr_dict)


def convert(map, start):
    for source, (length, dest) in map.items():
        if source <= start and source+length > start:
            return dest + (start-source)
    return start


def convert_range(map, r):
    start, s_len = r
    for source, (length, dest) in map.items():
        a = start
        b = start+s_len-1

        c = source
        d = source+length-1

        convert_factor = dest-c

        if a <= c and c <= b and b <= d:
            # print('type1', a, b, c, d)
            # c to b
            found = [(c + convert_factor, b-c+1)]
            # a to c-1
            looking = (a, c-a)

            rem_range = convert_range(map, looking)
            return found+rem_range
        if a <= c and d <= b:
            # print('type2', a, b, c, d)
            # c to d
            found = [(c + convert_factor, length)]
            # a to c-1
            looking = (a, c-a)
            rem_range = convert_range(map, looking)
            # d+1 to b
            looking2 = (d+1, b-d)
            rem_range2 = convert_range(map, looking2)
            return found+rem_range+rem_range2
        if c <= a and b <= d:
            # print('type3', a, b, c, d)
            # a to b
            found = [(a + convert_factor, s_len)]

            return found
        if c <= a and a <= d and d <= b:
            # print('type4', a, b, c, d)
            # a to d
            found = [(a + convert_factor, d-a+1)]
            # d+1 to b
            looking = (d+1, b-d)

            rem_range = convert_range(map, looking)
            return found+rem_range

    return [r]


lowest = 10**100
for s in seeds:
    curr_val = s
    for m in maps:
        curr_val = convert(m, curr_val)
    if curr_val < lowest:
        lowest = curr_val

print(lowest)


lowest = 10**100
for i in range(0, len(seeds), 2):

    curr_ranges = [(seeds[i], seeds[i+1])]
    for m in maps:
        # print(curr_ranges)
        new_ranges = []
        for r in curr_ranges:
            new_ranges += convert_range(m, r)
        curr_ranges = new_ranges

    curr_val = sorted(curr_ranges)[0][0]

    if curr_val < lowest:
        lowest = curr_val
