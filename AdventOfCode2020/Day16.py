from functools import reduce
import numpy as np


def read_nums(s):
    ranges = s.split(' or ')
    all_nums = set()
    for r in ranges:
        a, b = [int(x) for x in r.split('-')]
        all_nums |= set(range(a, b+1))
    return all_nums


def read_ticket(line):
    return [int(x) for x in line.split(',')]


fields = dict()
my_ticket = []
nearby_tickets = []

with open('input/input16.txt') as f:
    section = ''
    for line in f:
        line = line.strip()
        if line == 'your ticket:' or line == 'nearby tickets:':
            section = line
        elif len(line) > 0:
            if section == '':
                name, nums = line.split(': ')
                nums = read_nums(nums)
                fields[name] = nums
            elif section[0] == 'y':
                my_ticket = read_ticket(line)
            elif section[0] == 'n':
                nearby_tickets.append(read_ticket(line))

all_allowed_nums = reduce(lambda a, b: a | b, fields.values())

ticket_scanning_error_rate = 0
valid_tickets = [my_ticket]
for t in nearby_tickets:
    has_error = False
    for x in t:
        if x not in all_allowed_nums:
            has_error = True
            ticket_scanning_error_rate += x
    if not has_error:
        valid_tickets.append(t)


field_vals = np.array(valid_tickets).T
field_vals_sets = [set(x) for x in field_vals]

possible_names = []

for fvs in field_vals_sets:
    names = []
    for name, nums in fields.items():
        if len(fvs-nums) == 0:
            names.append(name)
    possible_names.append(names)


def remove(lists, name):
    new = []
    for row in lists:
        new.append([x for x in row if x != name])
    return new


correct_names = [None]*len(possible_names)
count = 0
while None in correct_names:
    count += 1
    for i, row in enumerate(possible_names):
        if len(row) == 1:
            correct_names[i] = row[0]
            possible_names = remove(possible_names, row[0])

tot = 1
for i in range(len(correct_names)):
    if correct_names[i].split(' ')[0] == 'departure':
        tot *= my_ticket[i]
print(tot)
