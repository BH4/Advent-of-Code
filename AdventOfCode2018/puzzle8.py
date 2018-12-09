"""
The tree object can be constructed and then recursive functions defined on the
tree object can be used to find solutions for both parts of the problem.
"""


class Tree(object):
    def __init__(self):
        self.children = []
        self.metadata = []

    def metadata_sum(self):
        """
        Recursively sum the metadata arrays for each node.
        """
        tot = sum(self.metadata)

        for child in self.children:
            tot += child.metadata_sum()

        return tot

    def value(self):
        """
        Recursively find the value for the given node.
        """
        num_children = len(self.children)
        if num_children == 0:
            return sum(self.metadata)

        tot = 0
        for m in self.metadata:
            if m > 0 and m <= num_children:
                tot += self.children[m-1].value()

        return tot


def tree_parse(vals, ind):
    """
    Given a list of values turn it into a tree with the requirement that each
    node is of the form
    num_children, num_metadata, ...numbers indicating children nodes..., metadata, metadata,...
    """
    t = Tree()

    next_child_ind = ind+2
    for child_num in range(vals[ind]):
        child, next_child_ind = tree_parse(vals, next_child_ind)
        t.children.append(child)

    t.metadata = vals[next_child_ind:next_child_ind+vals[ind+1]]

    return t, next_child_ind+vals[ind+1]


with open('input/input8.txt') as f:
    tree_string = f.readline()

tree_vals = [int(x) for x in tree_string.strip().split()]

root, _ = tree_parse(tree_vals, 0)

print("Sum of all metadata entries: {}".format(root.metadata_sum()))
print("Value of the root node: {}".format(root.value()))
