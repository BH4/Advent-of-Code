def find_same(s):
    """
    Find the one repeated character which is in the first half and last half of
    a string
    """

    sf = set(x for x in s[:len(s)//2])
    se = set(x for x in s[len(s)//2:])
    return list((sf & se))[0]


def find_badge(s1, s2, s3):
    s1 = set(x for x in s1)
    s2 = set(x for x in s2)
    s3 = set(x for x in s3)
    return list(s1 & s2 & s3)[0]


def priority_convert(c):
    o = ord(c)
    if ord('a') <= o <= ord('z'):
        return o-ord('a')+1

    return o-ord('A')+27


tot1 = 0
tot2 = 0
with open('input3.txt') as f:
    group = []
    for line in f:
        line = line.strip()
        tot1 += priority_convert(find_same(line))

        group.append(line)
        if len(group) == 3:
            badge = find_badge(*group)
            group = []
            tot2 += priority_convert(badge)


print(tot1)
print(tot2)
