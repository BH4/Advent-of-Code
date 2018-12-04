from collections import defaultdict
from time import sleep
#reg=[0]*26
reg=[defaultdict(int),defaultdict(int)]
"""
for i in xrange(26):
    reg[0][chr(i+ord('a'))]=0
    reg[1][chr(i+ord('a'))]=0
"""
def value(x,prog):
    try:
        return int(x)
    except:
        return reg[prog][x]

q=[[],[]]
numSent=[0,0]
def snd(x,prog):
    numSent[prog]+=1
    q[(prog+1)%2].append(value(x,prog))

def setf(x,y,prog):
    reg[prog][x]=value(y,prog)

def add(x,y,prog):
    reg[prog][x]+=value(y,prog)

def mul(x,y,prog):
    reg[prog][x]*=value(y,prog)

def mod(x,y,prog):
    reg[prog][x]=reg[prog][x]%value(y,prog)

def rcv(x,prog):
    reg[prog][x]=q[prog].pop(0)

def jgz(x,y,curr,prog):
    if value(x,prog)>0:
        return curr+value(y,prog)
    return curr+1


f=open('input/input18.txt')
instructions=[]
for line in f:
    c=line[:-1].split(' ')
    instructions.append(c)
f.close()

funcs={'snd':snd,'set':setf,'add':add,'mul':mul,'mod':mod}


#run this program until it hits a deadlock then run the other program until it hits a deadlock and so on.
#until nothing can happen
prog=0
curr=[0,0]
done=False
state=[1,1]#1 is good 0 is waiting
while not done:

    inst=instructions[curr[prog]]


    if inst[0]=='jgz':
        
        curr[prog]=jgz(inst[1],inst[2],curr[prog],prog)
    elif inst[0]=='rcv':
        if len(q[prog])>0:
            state[prog]=1
            rcv(inst[1],prog)
            curr[prog]+=1
        else:
            if sum(state)==0:
                done=True
            state[prog]=0
            prog=(prog+1)%2

    else:
        if len(inst)==3:
            funcs[inst[0]](inst[1],inst[2],prog)
        else:
            funcs[inst[0]](inst[1],prog)
        curr[prog]+=1


print numSent[1]/2#for some reason I get EXACTLY twice the value. Can't figure it out. I give up.