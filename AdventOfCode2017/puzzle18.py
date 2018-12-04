from time import sleep
#reg=[0]*26
reg={}
for i in xrange(26):
    reg[chr(i+ord('a'))]=0

def value(x):
    try:
        return int(x)
    except:
        return reg[x]


soundsPlayed=[]
def snd(x):
    soundsPlayed.append(value(x))

def setf(x,y):
    reg[x]=value(y)

def add(x,y):
    reg[x]+=value(y)

def mul(x,y):
    reg[x]*=value(y)

def mod(x,y):
    reg[x]=reg[x]%value(y)

def rcv(x):
    if value(x)!=0:
        return soundsPlayed[-1]

def jgz(x,y,curr):
    if value(x)>0:
        return curr+value(y)
    return curr+1


f=open('input/input18.txt')
instructions=[]
for line in f:
    c=line[:-1].split(' ')
    instructions.append(c)
f.close()

funcs={'snd':snd,'set':setf,'add':add,'mul':mul,'mod':mod}

curr=0
done=False
while not done:
    inst=instructions[curr]
    if inst[0]=='jgz':
        curr=jgz(inst[1],inst[2],curr)
    elif inst[0]=='rcv':
        val=rcv(inst[1])
        if not val is None:
            done=True
            print val
        else:
            curr+=1
    else:
        if len(inst)==3:
            funcs[inst[0]](inst[1],inst[2])
        else:
            funcs[inst[0]](inst[1])
        curr+=1

    #print reg
    #sleep(1)
