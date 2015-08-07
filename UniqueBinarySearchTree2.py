# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/8'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    def build_tree(array):
        result = []
        if len(array) == 0:
            return [None]
        if len(array) == 1:
            return [TreeNode(array[0])]
        for i in xrange(len(array)):
            left_sub_trees = build_tree(array[:i])
            right_sub_trees = build_tree(array[i+1:])
            for left_sub_tree in left_sub_trees:
                for right_sub_tree in right_sub_trees:
                    root = TreeNode(array[i])
                    root.left = left_sub_tree
                    root.right = right_sub_tree
                    result.append(root)
        return result
    return build_tree(range(1, n+1))


if __name__ == '__main__':
    print len(generateTrees(5))
    print len(generateTrees(6))
    print len(generateTrees(7))
