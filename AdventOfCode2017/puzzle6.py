
def nextState(state):
    curr=state.index(max(state))
    spare=state[curr]
    state[curr]=0

    curr=(curr+1)%len(state)
    while spare>0:
        state[curr]+=1
        spare-=1

        curr=(curr+1)%len(state)

    return state


previousStates=set()

state=[0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]

steps=0
while not tuple(state) in previousStates:
    previousStates.add(tuple(state))
    state=nextState(state)
    steps+=1

print steps

repeatedState=[x for x in state]
previousStates=set()
steps=0
while not tuple(state) in previousStates:
    previousStates.add(tuple(state))
    state=nextState(state)
    steps+=1

print steps