# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/14'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def rightSideView(root):
    result = []
    def helper(root, index):
        if not root:
            return
        if len(result) == index:
            result.append([])
        result[index].append(root.val)
        helper(root.left, index+1)
        helper(root.right, index+1)
    helper(root, 0)
    values = []
    for l in result:
        values.append(l[-1])
    return values

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right= TreeNode(5)
    root.right.right = TreeNode(4)
    print rightSideView(root)

