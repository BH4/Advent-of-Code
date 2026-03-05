from functools import reduce


problems = []
tot = 0
with open('input6.txt', 'r') as f:
    for line in f:
        line = line.strip()
        vals = line.split()

        try:
            vals = [int(x) for x in vals]
            if len(problems) == 0:
                problems = [[x] for x in vals]
            else:
                for i in range(len(vals)):
                    problems[i].append(vals[i])
        except:
            for i, s in enumerate(vals):
                if s == '*':
                    # print(problems[i])
                    tot += reduce(lambda x, y: x*y, problems[i])
                else:
                    tot += sum(problems[i])

print(tot)


signs = None
with open('input6.txt', 'r') as f:
    for line in f:
        signs = line.strip().split()


columns = []
tot = 0
with open('input6.txt', 'r') as f:
    count = 0
    for line in f:
        if count > 3:
            break
        line = line.strip()
        if len(columns) == 0:
            for i in range(len(line)):
                columns.append(line[i])

        else:
            for i in range(len(line)):
                columns[i] += line[i]


        count += 1

problems = []
curr = []
for v in columns:
    v = v.strip()
    if len(v) == 0:
        problems.append(curr)
        curr = []
    else:
        v = int(v)
        curr.append(v)

problems.append(curr)
tot = 0
for i, s in enumerate(signs):
    if s == '*':
        # print(problems[i])
        tot += reduce(lambda x, y: x*y, problems[i])
    else:
        tot += sum(problems[i])


print(tot)
