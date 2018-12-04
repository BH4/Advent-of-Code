import networkx as nx

def subgraphSize(G,start):
    connected=set()
    new=set([start])
    more=set()
    while len(new)>0:
        for curr in new:
            e=G.edges(curr)
            for c in e:
                if not c[1] in connected:
                    more.add(c[1])

            connected.add(curr)

        new=more
        more=set()

    return len(connected)



G=nx.Graph()
f=open('input/input12.txt')
for line in f:
    line=line.replace(',','')
    n=line.split(' ')
    node1=int(n[0])
    other=[int(x) for x in n[2:]]

    for o in other:
        G.add_edge(node1,o)

print subgraphSize(G,0)
print nx.number_connected_components(G)