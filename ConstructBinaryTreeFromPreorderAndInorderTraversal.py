# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/11'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def buildTree(preorder, inorder):
    length = len(inorder)
    preorder.reverse()
    def build_subtree(preorder, start, end):
        if not preorder or start > end:
            return None
        value = preorder.pop()
        node = TreeNode(value)
        index = inorder.index(value)
        node.left = build_subtree(preorder, start, index-1)
        node.right = build_subtree(preorder, index+1, end)
        return node
    root = build_subtree(preorder, 0, length-1)
    return root


if __name__ == '__main__':
    preorder = [1,2,4,8,9,5,3,6,7,]
    inorder = [8, 9, 4, 5, 2, 1, 6, 7, 3]
    print map(str, buildTree(preorder, inorder))
