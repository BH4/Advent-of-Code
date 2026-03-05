

with open('input6.txt') as f:
    for line in f:
        line = line.strip()

count = 4
curr = line[:4]
while len(set(curr)) != 4:
    curr = curr[1:]+line[count]
    count += 1

print(count)

count = 14
curr = line[:14]
while len(set(curr)) != 14:
    curr = curr[1:]+line[count]
    count += 1

print(count)
