def isValidPassphrase(s):
    temp=s.split(' ')
    return len(temp)==len(set(temp))

def isValidPassphrase2(s):
    temp=s.split(' ')
    words=[]
    for w in temp:
        words.append(''.join(sorted(w)))
    return len(words)==len(set(words))

f=open('input/input4.txt')

tot=0
tot2=0
for line in f:
    test=line[:-1]
    if isValidPassphrase(test):
        tot+=1
    if isValidPassphrase2(test):
        tot2+=1

f.close()
print tot
print tot2