"""
I solve the first and second parts of the puzzle simultaneously.
The first part is solved by keeping track of which spots have been used at
least twice. The second part is solved by keeping a list of good and bad ids
which correspond to ids that haven't overlapped and those that have.
"""


def get_used_locations(claim):
    """
    Return a list of tuples which each have (claim_id, (x, y))
    where (x, y) is a tuple representing a coordinate that is used by the
    claim with id claim_id.
    """

    claim = claim.strip()
    to_replace = ['#', '@', ',', ':', 'x']
    for r in to_replace:
        claim = claim.replace(r, ' ')

    claim_num, x_shift, y_shift, x, y = [int(v) for v in claim.split()]

    loc = []

    for i in range(x):
        for j in range(y):
            loc.append((claim_num, (x_shift+i, y_shift+j)))

    return loc


with open('input/input3.txt') as f:
    good_ids = set()
    bad_ids = set()
    used_once = dict()
    used_twice = set()

    for line in f:
        used = get_used_locations(line)

        for claim_id, coord in used:
            if coord in used_twice:
                # This coordinate has been used and is already in the list as
                # having been used twice. Note that this id is bad if it hasn't
                # been noted already.
                bad_ids.add(claim_id)
            elif coord in used_once:
                # Coord used once before. Need to add the coord to used twice
                # list and note that the new id and old one in this spot are
                # both bad. Also remove them from the good id list.
                used_twice.add(coord)

                bad_ids.add(claim_id)
                if claim_id in good_ids:
                    good_ids.remove(claim_id)

                old_id = used_once[coord]
                bad_ids.add(old_id)
                if old_id in good_ids:
                    good_ids.remove(old_id)
            else:
                # This spot hasn't been used yet. Attach this id to the
                # coordinate and if the id isn't bad add it to the good
                # id list.
                used_once[coord] = claim_id
                if claim_id not in bad_ids:
                    good_ids.add(claim_id)

print('The number of square inches used twice is {}'.format(len(used_twice)))  # 116491
print('The id of the claim with no overlap is {}'.format(list(good_ids)[0]))  # 707
