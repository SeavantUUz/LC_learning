# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/12'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


def buildTree(inorder, postorder):
    length = len(inorder)
    def build_subtree(postorder, start, end):
        if not postorder or start > end:
            return None
        value = postorder.pop()
        node = TreeNode(value)
        index = inorder.index(value)
        node.right = build_subtree(postorder, index+1, end)
        node.left = build_subtree(postorder, start, index-1)
        return node
    return build_subtree(postorder, 0, length-1)

