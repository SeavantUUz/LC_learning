# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/30'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def preorderTraversal(root):
    result = []
    def helper(root):
        if not root:
            return
        result.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print preorderTraversal(root)

