from collections import defaultdict


def apply_mask(num, mask):
    bin_value = bin(num)[2:]
    bin_value = '0'*(len(mask)-len(bin_value))+bin_value
    for i in range(len(mask)):
        if mask[i] != 'X':
            bin_value = bin_value[:i]+mask[i]+bin_value[i+1:]
    return int(bin_value, 2)


def apply_mask2(num, mask):
    bin_value = bin(num)[2:]
    bin_value = '0'*(len(mask)-len(bin_value))+bin_value
    final_list = ['']
    for i in range(len(mask)):
        if mask[i] == '0':
            final_list = [x+bin_value[i] for x in final_list]
        elif mask[i] == '1':
            final_list = [x+'1' for x in final_list]
        else:
            new_list = [x+'1' for x in final_list]
            new_list += [x+'0' for x in final_list]
            final_list = new_list

    return [int(x, 2) for x in final_list]


mem = defaultdict(int)
mem2 = defaultdict(int)
mask = ''
with open('input/input14.txt') as f:
    for line in f:
        line = line.strip()
        op, value = line.split(' = ')
        if op == 'mask':
            mask = value
        else:
            pos = int(op[4:-1])
            value = int(value)
            mem[pos] = apply_mask(value, mask)

            for p in apply_mask2(pos, mask):
                mem2[p] = value

print(sum(mem.values()))
print(sum(mem2.values()))
