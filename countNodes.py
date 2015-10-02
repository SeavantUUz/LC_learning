# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/3'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def countNodes0(root):
    from collections import Counter
    count = Counter()
    def helper(root):
        if not root:
            return
        if not root.left and not root.right:
            count['count'] += 1
            return
        else:
            helper(root.left)
            helper(root.right)
    helper(root)
    return count['count']


def countNodes(root):
    def height(root):
        if not root:
            return 0
        else:
            return 1 + height(root.left)

    h = height(root)
    if h <= 0:
        return 0
    else:
        r_h = height(root.right)
        if h == r_h + 1:
            return 2**(h-1) + countNodes(root.right)
        else:
            return 2**(h-2) + countNodes(root.left)

if __name__ == '__main__':
    node = TreeNode(1)
    print countNodes(node)