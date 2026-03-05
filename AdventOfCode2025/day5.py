
def is_fresh(ranges, x):
    for start, end in ranges:
        if start <= x <= end:
            return True
    return False


ranges = []
tot_fresh = 0
with open('input5.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break

        start, end = [int(x) for x in line.split('-')]
        ranges.append((start, end))

    for line in f:
        ingredient_id = int(line.strip())
        if is_fresh(ranges, ingredient_id):
            tot_fresh += 1
print(tot_fresh)

possible_fresh = 0
ranges.sort(key=lambda x: x[0])
last_end = 0
for start, end in ranges:
    if last_end < end:
        # print(end, start, last_end)
        possible_fresh += end-(max(start, last_end+1)-1)
        last_end = end

print(possible_fresh)
