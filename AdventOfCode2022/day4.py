tot1 = 0
tot2 = 0
with open('input4.txt') as f:
    group = []
    for line in f:
        line = line.strip()

        line = line.replace('-', ',')

        p = line.split(',')
        p = [int(x) for x in p]

        # if p[2] < p[0]:
        #     p = p[2:]+p[:2]


        if p[0] <= p[2] and p[1] >= p[3]:
            tot1 += 1
        elif p[2] <= p[0] and p[3] >= p[1]:
            tot1 += 1

        if p[0] <= p[2] and p[1] >= p[2]:
            tot2 += 1
        elif p[2] <= p[0] and p[3] >= p[0]:
            tot2 += 1

print(tot1)
print(tot2)


