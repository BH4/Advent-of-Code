
def reverse(nums,currInd,length):
    if length>len(nums) or length==1:
        return nums

    temp=nums[currInd:]+nums[:currInd]
    temp=temp[:length][::-1]+temp[length:]
    nums=temp[-currInd:]+temp[:-currInd]
    return nums

def oneRound(nums,currInd,skip,lengths):
    for l in lengths:
        nums=reverse(nums,currInd,l)
        currInd=(currInd+l+skip)%len(nums)
        skip+=1

    return nums,currInd,skip

def xor(nums):
    assert len(nums)==16
    result=nums[0]
    for i in xrange(1,len(nums)):
        result^=nums[i]
    return result

def getHex(num):
    h=hex(num)[2:]
    if len(h)==1:
        h='0'+h
    return h

nums=range(256)
currInd=0
skip=0
lengths=[189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62]
nums,_,_=oneRound(nums,currInd,skip,lengths)
print nums[0]*nums[1]


#part 2


nums=range(256)
currInd=0
skip=0

chars='189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'
lengths=[ord(x) for x in chars]+[17, 31, 73, 47, 23]

for i in xrange(64):
    nums,currInd,skip=oneRound(nums,currInd,skip,lengths)

denseHash=[xor(nums[16*i:16*(i+1)]) for i in xrange(16)]

KnotHash=''
for x in denseHash:
    KnotHash+=getHex(x)

print KnotHash