from collections import defaultdict

comparisons={'>':lambda x,y:x>y,'<':lambda x,y:x<y,'>=':lambda x,y:x>=y,'<=':lambda x,y:x<=y,'==':lambda x,y:x==y,'!=':lambda x,y:x!=y}

#reg is a defaltdict which initialized to integer 0 for unseen keys
def followInstruction(reg,instruction):
    w=instruction.split(' ')

    name=w[0]
    increase=(w[1]=='inc')
    amount=int(w[2])

    condition=comparisons[w[5]](reg[w[4]],int(w[6]))

    if condition:
        if increase:
            reg[name]+=amount
        else:
            reg[name]-=amount


reg=defaultdict(int)

biggestMax=0

f=open('input/input8.txt')
for line in f:
    if len(reg)>0:
        m=max(reg.values())
        if m>biggestMax:
            biggestMax=m

    instruction=line[:-1]
    followInstruction(reg,instruction)
f.close()


currMax=max(reg.values())
if currMax>biggestMax:
    biggestMax=currMax

print currMax
print biggestMax