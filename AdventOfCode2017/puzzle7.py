
#I just want to find the bottom program so all I need to do is find the program which is holding up others but
#is not being held up by others
notBottom=set()
maybeBottom=set()

f=open('input/input7.txt')
for line in f:
    temp=line[:-1].replace(',','')
    names=temp.split(' ')
    if len(names)>2:
        maybeBottom.add(names[0])

        for n in names[3:]:
            notBottom.add(n)
f.close()

print maybeBottom-notBottom
baseName=list(maybeBottom-notBottom)[0]


class tree:
    def __init__(self,name,weight):
        self.branches=[]
        self.weight=weight
        self.name=name

    def addBranch(self,other):
        self.branches.append(other)

    def addBranches(self,others):
        self.branches.extend(others)

    def getBranchNames(self):
        names=[]
        for b in self.branches:
            names.append(b.name)
        return names

    def getSubTreeWeight(self):
        tot=self.weight
        for b in self.branches:
            tot+=b.getSubTreeWeight()
        return tot

    def findWrongWeight(self):
        weights=[]
        for b in self.branches:
            weights.append(b.getSubTreeWeight())

        if len(set(weights))==1:
            return 0

        correctWeight=max(set(weights), key=weights.count)
        ind=0
        while weights[ind]==correctWeight:
            ind+=1

        ans=self.branches[ind].findWrongWeight()
        if ans==0:
            return self.branches[ind].weight-(weights[ind]-correctWeight)
        return ans

branchList={}#holds name of tree with an array of the names of branches
trees={}#name of tree and tree object

f=open('input/input7.txt')
for line in f:
    temp=line[:-1].replace(',','')
    names=temp.split(' ')

    curr=tree(names[0],int(names[1][1:-1]))
    trees[names[0]]=curr
    if len(names)>2:
        branchList[names[0]]=names[3:]
f.close()

for name in branchList:
    branches=branchList[name]
    curr=trees[name]

    curr.addBranches([trees[x] for x in branches])

base=trees[baseName]
print base.findWrongWeight()