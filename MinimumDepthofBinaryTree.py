# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/15'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)


def minDepth(root):
    if not root:
        return 0
    left_depth = minDepth(root.left)
    right_depth = minDepth(root.right)
    if left_depth != 0 and right_depth != 0:
        return  1+min(left_depth, right_depth)
    elif left_depth != 0:
        return 1+left_depth
    elif right_depth != 0:
        return 1+right_depth
    else:
        return 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(20)
    print minDepth(root)
