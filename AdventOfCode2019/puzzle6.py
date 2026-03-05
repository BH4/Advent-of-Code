from collections import defaultdict


class tree:
    def __init__(self, name):
        self.leaves = []
        self.name = name

    def add_leaf(self, name):
        t = tree(name)

        self.leaves.append(t)

    def build_from_dict(self, d):
        for leaf_name in d[self.name]:
            t = tree(leaf_name)
            t.build_from_dict(d)
            self.leaves.append(t)

    def direct_orbits(self):
        tot = 0
        for leaf in self.leaves:
            tot += leaf.direct_orbits()+1
        return tot

    def all_orbits(self, depth):
        tot = depth
        for leaf in self.leaves:
            tot += leaf.all_orbits(depth+1)
        return tot

    def depth_of_name(self, name):
        if self.name == name:
            return 0

        for leaf in self.leaves:
            result = leaf.depth_of_name(name)
            if result is not None:
                return result + 1

        return None

    def common_node_depth(self, name1, name2):
        for leaf in self.leaves:
            depth1 = leaf.depth_of_name(name1)
            depth2 = leaf.depth_of_name(name2)

            if depth1 is not None and depth2 is not None:
                return leaf.common_node_depth(name1, name2) + 1
            elif depth1 is not None or depth2 is not None:
                return 0

        return None

    def orbit_transfers(self, name1, name2):
        depth1 = self.depth_of_name(name1)
        depth2 = self.depth_of_name(name2)
        c = self.common_node_depth(name1, name2)

        return (depth1-c-1)+(depth2-c-1)


orbits = defaultdict(list)

not_com = set()
with open('input/input6.txt', 'r') as f:
    for line in f:
        line = line.strip()
        a, b = line.split(')')

        not_com.add(b)

        orbits[a].append(b)


com = list(set(orbits.keys())-not_com)[0]

root = tree(com)
root.build_from_dict(orbits)

print(root.all_orbits(0))
print(root.orbit_transfers('YOU', 'SAN'))
