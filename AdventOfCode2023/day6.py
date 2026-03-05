import numpy as np

T = [50, 74, 86, 85]
D = [242, 1017, 1691, 1252]


def get_zeros(t, d):
    v = np.sqrt(t**2-4*d)
    return ((t-v)/2, (t+v)/2)


def get_ways(t, d):
    a, b = get_zeros(t, d)
    a = int(a+1)
    b = int(b)
    n = b-a+1
    return n


prod = 1
for i in range(4):
    n = get_ways(T[i], D[i])
    prod *= n
print(prod)


print(get_ways(50748685, 242101716911252))
