
def invalid_in_range(a, b):
    """
    Return list of integers from a to b inclusive which are "invalid".
    Invalid integers are those which are some integer concatenated with itself.
    e.g. 55, 123123, 789456789456

    Equivalently, these integers are a product of 11, 101, 1001, ect. with a
    1, 2, 3, ect digit number.

    This was an unnecessary fancy way to do the first part. Certainly faster
    but brute force was fast enough.
    """
    sa = str(a)
    sb = str(b)
    if len(sa) == len(sb) and len(sa) % 2 == 1:
        return []

    invalid = []
    for length in range(len(sa), len(sb)+1):
        if length % 2 == 1:
            continue

        half_len = length//2

        # number to multiply by to get the invalid
        mult = 10**half_len+1

        low = max(mult*(10**(half_len-1)), a)//mult
        high = min(mult*(10**half_len-1), b)//mult

        for v in range(low, high+1):
            test = v*mult
            if a <= test <= b:
                # print(length, low, high, a, b, test, mult, v)
                invalid.append(test)
    return invalid


def is_invalid1(x):
    sx = str(x)
    if len(sx) % 2 == 1:
        return False

    s = len(sx)//2
    if sx[:s] == sx[s:]:
        return True
    return False


def brute1(a, b):
    tot = 0
    for x in range(a, b+1):
        if is_invalid1(x):
            tot += x
    return tot


def is_invalid2(x):
    sx = str(x)

    s = len(sx)//2
    for sub_len in range(1, s+1):
        if len(sx) % sub_len != 0:
            # This length can't divide evenly into the full one
            continue

        repeats = len(sx)//sub_len

        if sx[:sub_len]*repeats == sx:
            return True

    return False


def brute2(a, b):
    tot = 0
    for x in range(a, b+1):
        if is_invalid2(x):
            tot += x
    return tot


tot1 = 0
tot2 = 0
with open('input2.txt', 'r') as f:
    line = f.readline()
    # line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    line = line.strip()
    range_string = line.split(',')
    ranges = [[int(x) for x in s.split('-')] for s in range_string]

    for a, b in ranges:
        tot1 += brute1(a, b)
        tot2 += brute2(a, b)
print(tot1)
print(tot2)
