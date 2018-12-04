"""
The first puzzle for day 1 is essentially asking us to sum all the numbers
in the given file.
"""

with open('input/input1.txt') as f:
    tot = 0
    for num in f:
        tot += int(num)

print("The resulting frequency is {}".format(tot))


"""
A simple way to solve the second puzzle is to loop through the frequency
changes continuously (while saving each current frequency in a set) until the
current frequency already exists in the set.
Using a set here is more efficient than a list because it can check if an
element exists in the set in constant time (on average).
"""

# Create a list of all the input values in case it needs to be looped over
delta_list = []
with open('input/input1.txt') as f:
    for num in f:
        delta = int(num)
        delta_list.append(delta)


# Set to keep track of all values seen earlier
seen = set()
seen.add(0)

# Track current frequency as well as the index of the next change in frequency
curr_freq = 0
ind = 0

# Loop until I find a duplicate frequency
done = False
while not done:
    curr_freq += delta_list[ind]

    if curr_freq in seen:
        # Found duplicate, set flag
        done = True
    else:
        # No duplicates
        seen.add(curr_freq)
        ind = (ind+1) % len(delta_list)

print("The first frequency reached twice is {}".format(curr_freq))
