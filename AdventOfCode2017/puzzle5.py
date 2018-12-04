def numSteps(instructions):
    curr=0

    steps=0
    while curr<len(instructions):
        jump=instructions[curr]


        instructions[curr]+=1
        curr+=jump
        steps+=1

    return steps

def numSteps2(instructions):
    curr=0

    steps=0
    while curr<len(instructions):
        jump=instructions[curr]

        if jump>=3:
            instructions[curr]-=1
        else:
            instructions[curr]+=1

        curr+=jump
        steps+=1

    return steps

instructions=[]
f=open('input/input5.txt')
for line in f:
    instructions.append(int(line[:-1]))
f.close()


#print numSteps(instructions)
print numSteps2(instructions)

#print numSteps2([0,3,0,1,-3])
