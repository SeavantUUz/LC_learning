# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/10'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def maxDepth(root):
    def depth(root):
        if not root:
            return 0
        return max(1+depth(root.left), 1+depth(root.right))
    return depth(root)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    print maxDepth(root)
