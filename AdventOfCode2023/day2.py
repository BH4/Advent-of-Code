import re


types = [r'(\d*) red', r'(\d*) green', r'(\d*) blue']
limit = [12, 13, 14]


def read_set_color_nums(s):
    vs = []
    for c in types:
        vl = re.findall(c, s)
        v = 0
        if len(vl) == 1:
            v = int(vl[0])
        elif len(vl) > 1:
            print('bad')
            quit()
        vs.append(v)
    return vs


def is_possible(s):
    for m, v in zip(limit, read_set_color_nums(s)):
        if m < v:
            return False
    return True


def min_game_power(s_list):
    """
    Return minimum number of cubes for each color for entire game
    """
    m = [0, 0, 0]
    for s in s_list:
        vs = read_set_color_nums(s)
        for i, v in enumerate(vs):
            if v > m[i]:
                m[i] = v

    return m[0]*m[1]*m[2]


tot_inds = 0
tot_power = 0
with open('input/input2.txt') as f:

    for line in f:
        line = line.strip()
        game, sets = line.split(': ')
        my_id = int(game[5:])

        sets = sets.split('; ')

        allowed_game = True
        for s in sets:
            if not is_possible(s):
                allowed_game = False
                break
        if allowed_game:
            tot_inds += my_id

        tot_power += min_game_power(sets)

print(tot_inds)
print(tot_power)
