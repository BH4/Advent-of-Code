
rules = dict()
with open('input/input7.txt') as f:
    for line in f:
        # all lines end in period and new line
        outside, inside = line.strip()[:-1].split(' bags contain ')
        inside = inside.split(', ')
        bags = []
        if inside == ['no other bags']:
            rules[outside] = []
        else:
            for bag in inside:
                num = int(bag[0])
                # all have one digit
                assert bag[1] == ' '

                if num > 1:
                    color = bag[2:-5]
                else:
                    color = bag[2:-4]
                bags.append((num, color))
            rules[outside] = bags



my_bag = 'shiny gold'
mem = {}
def contains(color):
    if color not in rules or len(rules[color]) == 0:
        return False

    if color not in mem:
        mem[color] = False
        for c2 in rules[color]:
            c2 = c2[1]
            if c2 == my_bag or contains(c2):
                mem[color] = True
                break

    return mem[color]


can_contain = 0
for color in rules.keys():
    if contains(color):
        can_contain += 1
print(can_contain)


def bags_within(color):
    num = 0
    for n, c2 in rules[color]:
        num += n+n*bags_within(c2)
    return num


print(bags_within(my_bag))
