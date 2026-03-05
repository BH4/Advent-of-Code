import re


class G:
    def __init__(self, name):
        self.name = name

    def lr(self, left, right):
        self.left = left
        self.right = right


with open('input/input8.txt') as f:
    end_A = set()
    end_Z = set()
    inst = f.readline().strip()
    f.readline()

    nodes = dict()
    for line in f:
        line = line.strip()
        n, L, R = re.findall(r'(.*) = \((.*), (.*)\)', line)[0]
        if n[-1] == 'A':
            end_A.add(n)
        if n[-1] == 'Z':
            end_Z.add(n)

        if L in nodes:
            lg = nodes[L]
        else:
            lg = G(L)

        if R in nodes:
            rg = nodes[R]
        else:
            rg = G(R)

        if n in nodes:
            ng = nodes[n]
        else:
            ng = G(n)
            nodes[n] = ng

        ng.lr(lg, rg)


curr = 'AAA'
i = 0
while curr != 'ZZZ':
    if inst[i % len(inst)] == 'L':
        curr = nodes[curr].left.name
    if inst[i % len(inst)] == 'R':
        curr = nodes[curr].right.name

    i += 1

print(i)

"""
def gn(c, lr):
    if lr == 'L':
        return nodes[c].left.name
    if lr == 'R':
        return nodes[c].right.name
    quit()


curr = list(end_A)
i = 0
all_z = False
while not all_z:
    all_z = True
    new = []
    for c in curr:
        d = gn(c, inst[i % len(inst)])
        new.append(d)
        if d not in end_Z:
            all_z = False

    i += 1

print(i)
"""
print(len(end_Z))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Compute the lowest common multiple of a and b
def lcm(a, b):
    return (a * b) // gcd(a, b)


def cycle(curr):
    i = 0
    while i < 100000:
        if inst[i % len(inst)] == 'L':
            curr = nodes[curr].left.name
        if inst[i % len(inst)] == 'R':
            curr = nodes[curr].right.name

        i += 1

        if curr in end_Z:  # happens to only be one z for each A
            return i

c = None
for a in list(end_A):
    if c is None:
        c = cycle(a)
    else:
        c = lcm(c, cycle(a))

print(c)
