
code = []
with open('input/input8.txt') as f:
    for line in f:
        instruction, num = line.strip().split()
        num = int(num)
        code.append((instruction, num))


def run_code(code):
    acc = 0
    ind = 0
    used = set()
    while ind not in used and ind < len(code):
        used.add(ind)

        inst, num = code[ind]
        if inst == 'acc':
            acc += num
            ind += 1
        elif inst == 'jmp':
            ind += num
        else:
            ind += 1

    if ind == len(code):
        inf = False
    else:
        inf = True
    return acc, inf


print(run_code(code)[0])


for i in range(len(code)):
    inst, num = code[i]
    if inst == 'nop':
        code[i] = ('jmp', num)
        acc, inf = run_code(code)
        if not inf:
            print(acc)
            break
        code[i] = ('nop', num)
    elif inst == 'jmp':
        code[i] = ('nop', num)
        acc, inf = run_code(code)
        if not inf:
            print(acc)
            break
        code[i] = ('jmp', num)

