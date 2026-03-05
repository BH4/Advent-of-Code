valid1 = 0
valid2 = 0

with open('input/input2.txt') as f:
    for line in f:
        policy, password = line.strip().split(': ')

        min_n, other = policy.split('-')
        max_n, letter = other.split()
        min_n = int(min_n)
        max_n = int(max_n)

        # password is valid if 'letter' appears between min_n and max_n times
        if min_n <= password.count(letter) <= max_n:
            valid1 += 1

        # password is valid if 'letter' appears at min_n xor max_n
        if (password[min_n-1] == letter) ^ (password[max_n-1] == letter):
            valid2 += 1

print('Puzzle 1:', valid1)
print('Puzzle 2:', valid2)
