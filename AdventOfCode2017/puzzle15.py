
criteria=True

def nextValA(c):
    n=(c*16807)%2147483647
    while criteria and n%4!=0:
        n=(n*16807)%2147483647
    return n

def nextValB(c):
    n=(c*48271)%2147483647
    while criteria and n%8!=0:
        n=(n*48271)%2147483647
    return n

def judge(a,b):
    if a>=2**15:
        last16A=bin(a)[-16:]
    else:
        last16A=bin(a)[2:]
        while len(last16A)<16:
            last16A='0'+last16A

    if b>=2**15:
        last16B=bin(b)[-16:]
    else:
        last16B=bin(b)[2:]
        while len(last16B)<16:
            last16B='0'+last16B

    return last16A==last16B


currA=783
currB=325

lim=40000000
if criteria:
    lim=5000000

tot=0
for i in xrange(lim):
    if i%1000000==0:
        print i

    currA=nextValA(currA)
    currB=nextValB(currB)
    if judge(currA,currB):
        tot+=1

print tot