from collections import defaultdict


splits = 0
beams = defaultdict(int)
with open('input7.txt', 'r') as f:
    for line in f:
        line = line.strip()

        new_beams = defaultdict(int)
        if len(beams) == 0 and 'S' in line:
            new_beams[line.index('S')] += 1
        else:
            for i, count in beams.items():
                if line[i] == '^':
                    splits += 1
                    new_beams[i-1] += count
                    new_beams[i+1] += count
                else:
                    new_beams[i] += count

        beams = new_beams

print(splits)
print(sum(beams.values()))
