
def score(s):
    tot=0

    inside=0#counts number of groups i am inside
    for c in s:
        if c=='{':
            inside+=1
            tot+=inside
        if c=='}':
            inside-=1

    assert inside==0
    return tot





f=open('input/input9.txt')
s=f.read()
f.close()

#print len(s)

#delete ! and the character following it in order.
i=0
done=False
while i<len(s):
    if s[i]=='!':
        s=s[:i]+s[i+2:]
    else:
        i+=1

#print len(s)

#delete garbage <>. could combine with previous loop to make it faster. only matters if i have super long input.
i=0
garbageStart=-1#not in garbage yet
countGarbageChars=0
while i<len(s):
    if s[i]=='<' and garbageStart==-1:
        garbageStart=i
    elif garbageStart>=0 and s[i]=='>':
        countGarbageChars+=i-garbageStart-1

        s=s[:garbageStart]+s[i+1:]
        i=garbageStart
        garbageStart=-1
    else:
        i+=1

#print len(s)

print score(s)
print countGarbageChars