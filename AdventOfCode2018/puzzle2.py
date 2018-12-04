"""
For the first problem we wish to count all the strings which have any letters
with frequency 2 or 3. My implementation just calculates the frequency of all
letters in each string and checks if 2 or 3 are among the frequencies.
"""

# Default dictionaries allow me to skip the step of checking if a particular
# letter has already appeared.
from collections import defaultdict


def frequency(s):
    """
    Return a list which contains the number of times each letter appears in s
    """
    f = defaultdict(int)
    for letter in s:
        f[letter] += 1

    return f.values()


num_with_two = 0
num_with_three = 0
with open('input/input2.txt') as f:
    for line in f:
        counts = frequency(line)
        if 2 in counts:
            num_with_two += 1
        if 3 in counts:
            num_with_three += 1

checksum = num_with_two*num_with_three
print("The checksum value is {}".format(checksum))

"""
My implementation for the second problem should be O(n) runtime, whereas the
simpler approach of comparing each sting to every other string would be O(n^2).

This approach assumes all the strings are of equal length and there is only one
solution.

I create a list of sets where each set corresponds to a position in the
strings. I then loop through all the strings and create a new set of strings
each missing one letter from the original and add it to the corresponding set.
If I ever find a duplicate then I have found the solution.
"""


def find_similar():
    # List that will contain the sets of strings with one missing letter
    one_missing_letter_sets = []
    with open('input/input2.txt') as f:
        for line in f:
            # Remove the newline character
            line = line.strip()

            # Need to initialize the list with the correct number of sets
            if len(one_missing_letter_sets) == 0:
                one_missing_letter_sets = [set() for i in range(len(line))]

            for i in range(len(line)):
                test = line[:i]+line[i+1:]

                if test in one_missing_letter_sets[i]:
                    return test
                else:
                    one_missing_letter_sets[i].add(test)


ans = find_similar()
print("The common letters between the two correct box ids are {}".format(ans))
