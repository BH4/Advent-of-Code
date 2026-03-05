f = open('input/input15.txt')
steps = f.read().strip().split(',')
f.close()


def hash(s):
    curr = 0
    for c in s:
        curr += ord(c)
        curr = (curr*17) % 256
    return curr



boxes = [[] for i in range(256)]
tot_hash = 0
for s in steps:
    h = hash(s)
    tot_hash += h

    if '-' in s:
        label = s[:-1]
        box = hash(label)
        for lens in boxes[box]:
            if label == lens[0]:
                boxes[box].remove(lens)
                break
    if '=' in s:
        label, val = s.split('=')
        box = hash(label)
        val = int(val)
        added = False
        for lens in boxes[box]:
            if label == lens[0]:
                lens[1] = val
                added = True
                break
        if not added:
            boxes[box].append([label, val])


print(tot_hash)



tot_focus = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        tot_focus += (i+1)*(j+1)*lens[1]

print(tot_focus)

