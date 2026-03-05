
count_0 = 0
count_all_0 = 0
curr = 50
with open('input1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        d = line[0]
        n = int(line[1:])

        count_all_0 += n//100

        n %= 100

        if d == 'L':
            if n >= curr and curr != 0:
                count_all_0 += 1
            curr -= n
        elif d == 'R':
            if n+curr >= 100:
                count_all_0 += 1
            curr += n

        curr %= 100

        if curr == 0:
            count_0 += 1

print(count_0)
print(count_all_0)
