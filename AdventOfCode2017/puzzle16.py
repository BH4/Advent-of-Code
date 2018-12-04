


def spin(s,n):
    return s[-n:]+s[:-n]

def exchange(s,i,j):
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    return s

def partner(s,a,b):
    inda=s.index(a)
    indb=s.index(b)
    return exchange(s,inda,indb)

def doMoves(start,moves):
    curr=[x for x in start]

    for m in moves:
        if m[0]=='s':
            curr=spin(curr,int(m[1:]))
            if int(m[1])>=10:
                print 'adf'

        if m[0]=='x':
            first,second=m[1:].split('/')
            curr=exchange(curr,int(first),int(second))

        if m[0]=='p':
            first,second=m[1:].split('/')
            curr=partner(curr,first,second)

    return curr

def concat(curr):
    ans=''
    for c in curr:
        ans+=c

    return ans


start=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

f=open('input/input16.txt')
moves=f.read().split(',')
f.close()

print concat(doMoves(start,moves))




curr=[x for x in start]
mem=dict()
mem[concat(start)]=0
mem2=[concat(start)]
i=0
limit=10**9
while i<limit:
    i+=1

    n=doMoves(curr,moves)
    if concat(n) in mem:
        loopSize=i-mem[concat(n)]
        print mem2[(limit-i)%loopSize+mem[concat(n)]]
        i=limit+1

    else:
        mem[concat(n)]=i
        mem2.append(concat(n))
    
    curr=n


