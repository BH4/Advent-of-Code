from collections import defaultdict


def works(n):
    last = 0
    repeat = False
    for i in str(n):
        if int(i) < last:
            return False
        if int(i) == last:
            repeat = True

        last = int(i)

    return repeat


def works2(n):
    prev_last = 0
    last = 0
    repeat = False
    for i, x in enumerate(str(n)):
        if int(x) < last:
            return False

        #print(n, i, x)
        if int(x) == last and int(x) != prev_last and (i == len(str(n))-1 or int(x) != int(str(n)[i+1])):
            repeat = True

        prev_last = last
        last = int(x)

    return repeat


#print(works2(77888))

tot = 0
for i in range(254032, 789860+1):
    if works(i):
        tot += 1

print(tot)


tot = 0
for i in range(254032, 789860+1):
    if works2(i):
        tot += 1

print(tot)

