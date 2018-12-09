"""
I have written a function which "reacts" the string completely.
This immediately solve the first part.
"""


def full_react(polymer):
    """
    Remove two characters if they appear adjacent in upper and lower case and
    are the same letter. Applied such that if a new example is created it is
    also removed.
    """
    i = 0
    while i < len(polymer)-1:
        u1 = polymer[i]
        u2 = polymer[i+1]

        if u1.lower() == u2.lower():
            if (u1.islower() and u2.isupper()) or (u2.islower() and u1.isupper()):
                polymer = polymer[:i]+polymer[i+2:]
                i = max(0, i-1)
            else:
                i += 1
        else:
            i += 1

    return polymer


with open('input/input5.txt') as f:
    polymer = f.readline()
polymer = polymer.strip()


basic_polymer_react = full_react(polymer)

print("Length of reacted polymer: {}".format(len(basic_polymer_react)))


"""
The second part can be solved by applying the function from the first part to
the full string with all of a specific letter removed. Doing this for each
letter and keeping track of the shortest solution allows us to find the answer.
"""

best_len = len(basic_polymer_react)
for i in range(26):
    curr = chr(ord('a')+i)
    polymer_missing_curr = polymer.replace(curr, '').replace(curr.upper(), '')
    polymer_react = full_react(polymer_missing_curr)
    p_len = len(polymer_react)
    if p_len < best_len:
        best_len = p_len

print("Minimal reacted polymer length with one letter removed: {}".format(best_len))
