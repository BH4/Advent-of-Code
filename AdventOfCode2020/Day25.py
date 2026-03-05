
def transform(loop_size):
    return pow(7, loop_size, 20201227)


public_keys = [11404017, 13768789]

"""
loop_sizes = []
i = 1
while len(public_keys) > 0:
    t = transform(i)
    if t in public_keys:
        loop_sizes.append(i)
        public_keys.remove(t)
        print(i)
    i += 1

    if i % 10**6 == 0:
        print(i)

print(loop_sizes)
"""
loop_sizes = [8516638, 11710225]
print(transform(loop_sizes[0]))
print(transform(loop_sizes[1]))
print(transform(loop_sizes[0]*loop_sizes[1]))
