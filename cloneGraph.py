# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/25'


class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def cloneGraph(node):
    memo = dict()
    def get_new_node(label):
        if not label in memo:
            node = UndirectedGraphNode(label)
            memo[label] = node
        return memo[label]

    def clone_helper(orig_node, new_node):
        if not orig_node:
            return
        neighbors = orig_node.neighbors
        for child in neighbors:
            label = child.label
            if label not in memo:
                new_child = UndirectedGraphNode(label)
                memo[label] = new_child
                clone_helper(child, new_child)
            else:
                new_child = memo[label]
            new_node.neighbors.append(new_child)

    if not node:
        return None
    label = node.label
    new_node = get_new_node(label)
    clone_helper(node, new_node)
    return new_node
