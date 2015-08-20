# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/20'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def sumNumbers(root):
    result = []
    def dp(root, value):
        if not root:
            return 0
        left = root.left
        right = root.right
        if not left and not right:
            result.append(10*value + root.val)
        else:
            dp(left, 10*value + root.val)
            dp(right, 10*value + root.val)
    dp(root, 0)
    return sum(result)


if __name__ == '__main__':
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    print sumNumbers(root)
