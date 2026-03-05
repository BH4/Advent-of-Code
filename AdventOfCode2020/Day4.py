def add_data(d, data):
    for entry in data.split():
        key, value = entry.split(':')
        d[key] = value


def all_present(d):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for r in required:
        if r not in d:
            return False
    return True


def is_int_between(test, low, high):
    try:
        num = int(test)
        return low <= num <= high
    except ValueError:
        return False


def is_valid(d):
    if not len(d['byr']) == 4 or not is_int_between(d['byr'], 1920, 2002):
        return False
    if not len(d['byr']) == 4 or not is_int_between(d['iyr'], 2010, 2020):
        return False
    if not len(d['byr']) == 4 or not is_int_between(d['eyr'], 2020, 2030):
        return False

    hgt = d['hgt']
    if hgt[-2:] == 'in':
        if not is_int_between(hgt[:-2], 59, 76):
            return False
    elif hgt[-2:] == 'cm':
        if not is_int_between(hgt[:-2], 150, 193):
            return False
    else:
        return False

    hcl = d['hcl']
    nums = [str(x) for x in range(10)]
    lets = list('abcdef')
    allow = nums+lets
    if hcl[0] != '#' or not all([x in allow for x in hcl[1:]]) or len(hcl) != 7:
        return False

    if d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    pid = d['pid']
    if len(pid) != 9 or not is_int_between(pid, 0, 999999999):
        return False

    return True



passports = []

with open('input/input4.txt') as f:
    curr = {}
    for line in f:
        if len(line.strip()) > 0:
            add_data(curr, line.strip())
        else:
            passports.append(curr)
            curr = {}
    if len(curr) > 0:
        passports.append(curr)

num_present = 0
num_valid = 0
for p in passports:
    if all_present(p):
        num_present += 1
        if is_valid(p):
            num_valid += 1

print(num_present)
print(num_valid)
