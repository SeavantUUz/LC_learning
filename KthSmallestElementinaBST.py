# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/11'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def kthSmallest(root, k):
    stack = []
    while root:
        stack.append(root)
        root = root.left
    k = k - 1
    while k:
        node = stack.pop()
        if node.right:
            n = node.right
            while n:
                stack.append(n)
                n = n.left
        k -= 1
    r = stack.pop()
    return r.val


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print kthSmallest(root, 4)

