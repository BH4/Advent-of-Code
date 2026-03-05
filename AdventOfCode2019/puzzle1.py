
module_fuel = 0
with open('input/input1.txt', 'r') as f:
    for line in f:
        n = int(line)
        fuel = n//3-2
        module_fuel += fuel

print(module_fuel)


# part 2 ----------------------------------------------------------------------
def fuel_calc(n):
    new = n
    tot = 0
    while new > 0:
        f = new//3-2
        if f > 0:
            tot += f
        new = f

    return tot


tot_fuel = 0
with open('input/input1.txt', 'r') as f:
    for line in f:
        n = int(line)
        tot_fuel += fuel_calc(n)

print(tot_fuel)
