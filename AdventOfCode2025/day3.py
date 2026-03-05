

def line_max(line):
    vals = [int(x) for x in line]
    first_digit = max(vals[:-1])
    first_ind = vals.index(first_digit)
    second_digit = max(vals[first_ind+1:])
    return first_digit*10+second_digit


def line_max2(line):
    vals = [int(x) for x in line]
    result = 0
    remaining_digits = 12
    while remaining_digits > 0:
        # print(vals, remaining_digits, result)
        if remaining_digits > 1:
            next_digit = max(vals[:-1*(remaining_digits-1)])
        else:
            next_digit = max(vals)
        next_ind = vals.index(next_digit)
        vals = vals[next_ind+1:]
        result = result*10+next_digit

        remaining_digits -= 1

    return result


tot = 0
tot2 = 0

with open('input3.txt', 'r') as f:
    for line in f:
        line = line.strip()
        tot += line_max(line)
        tot2 += line_max2(line)

print(tot)
print(tot2)
