



ranges={}
#scannerLocations={}
f=open('input/input13.txt')
for line in f:
    s=line.split(': ')
    ranges[int(s[0])]=int(s[1])
    #scannerLocations[int(s[0])]=0
f.close()

IamCaught=lambda depth,offset,sRange:(depth+offset)%(2*(sRange-1))==0

severity=0
for k in ranges.keys():
    if IamCaught(k,0,ranges[k]):
        severity+=k*ranges[k]

print severity

offset=0
caught=True
while caught:
    caught=False
    offset+=1
    
    for k in ranges.keys():
        if IamCaught(k,offset,ranges[k]):
            caught=True
            break

print offset