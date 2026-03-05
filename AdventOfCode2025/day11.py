# I'm assuming its an interconnected tree instead of a graph
class tree:
    def __init__(self, name):
        self.name = name
        self.leaves = []

        self.memo_path = dict()

    def add_leaf(self, other_tree):
        self.leaves.append(other_tree)

    def path_count(self, end):
        # print(self.name, end, [x.name for x in self.leaves])
        if self.name == end:
            return 1
        if end in self.memo_path:
            return self.memo_path[end]

        count = 0
        for leaf in self.leaves:
            count += leaf.path_count(end)

        self.memo_path[end] = count
        return count

    def path_count_reqs(self, end, reqs):
        # To be included the path must see all names in reqs before end
        # reqs is a list of strings
        reqs = [x for x in reqs]
        if self.name in reqs:
            reqs.remove(self.name)

        if len(reqs) == 0:
            return self.path_count(end)

        if (end, tuple(reqs)) in self.memo_path:
            return self.memo_path[(end, tuple(reqs))]

        count = 0
        for leaf in self.leaves:
            count += leaf.path_count_reqs(end, reqs)

        self.memo_path[(end, tuple(reqs))] = count
        return count


devices = dict()
with open('input11.txt', 'r') as f:
    for line in f:
        line = line.strip()
        data = line.split(' ')

        start_name = data[0][:-1]
        end_names = data[1:]

        if start_name in devices:
            curr_tree = devices[start_name]
        else:
            curr_tree = tree(start_name)
            devices[start_name] = curr_tree

        for e in end_names:
            if e in devices:
                curr_leaf = devices[e]
            else:
                curr_leaf = tree(e)
                devices[e] = curr_leaf

            curr_tree.add_leaf(curr_leaf)


print(devices['you'].path_count('out'))
print(devices['svr'].path_count_reqs('out', ['dac', 'fft']))
