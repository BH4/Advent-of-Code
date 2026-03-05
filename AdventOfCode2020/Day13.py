earliest = 1002618
busses = '19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,367,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'
busses = busses.split(',')
busses = [(int(busses[i]), i) for i in range(len(busses)) if busses[i] != 'x']


best = 0
time = 1000
for n, i in busses:
    t = n-earliest % n
    if t < time:
        time = t
        best = n
print(time*best)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


# Extended Euclidean algorithm. u and v are one set of solutions to
# a*u+b*v=GCD(a, b) and r=GCD(a, b)
def ExtendedEuclidean(a, b):
    r = a
    r2 = b
    u = 1
    v = 0
    u2 = 0
    v2 = 1
    while r2 != 0:
        q = r//r2
        rs = r
        us = u
        vs = v
        r = r2
        u = u2
        v = v2
        r2 = rs - q*r2
        u2 = us - q*u2
        v2 = vs - q*v2

    return (r, u, v)

# returns the minimal non-negative solution to the set of equations
# x = a mod m
# x = b mod n
# with m and n coprime and 
# 531
def ChineseRemainderTheorem(a, m, b, n):
    g, u, v = ExtendedEuclidean(m, n)
    if not (a % g == b % g):
        return None

    # there is only one solution between 0 and lcm(m, n)-1 inclusive
    x = ((a*v*n+b*u*m)//g) % lcm(m, n)

    return x

# Given a set of equations
# x = a_i mod m_i
# Return the x that satisfies all of them and is less than the product of all
# m_i. The m_i must be relatively prime. The above function
# "ChineseRemainderTheorem" is applied iteratively.
def GeneralChineseRemainderTheorem(remainders, mods):
    if len(remainders) != len(mods) or len(mods) <= 1:
        return None

    i = 0
    a_old = remainders[i]
    m_old = mods[i]
    i += 1

    while i < len(remainders):
        a_new = remainders[i]
        m_new = mods[i]
        i += 1

        x = ChineseRemainderTheorem(a_old, m_old, a_new, m_new)

        a_old = x
        m_old = m_old*m_new

    return x


remainders = []
mods = []
for n, i in busses:
    remainders.append((n-i) % n)
    mods.append(n)

print(GeneralChineseRemainderTheorem(remainders, mods))
