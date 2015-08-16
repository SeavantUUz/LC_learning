# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/16'

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.val)

def connect(root):
    stacks = []
    if not root:
        return
    def subtree_connect(root, level):
        if not root:
            return
        if level == len(stacks):
            stacks.append([])
            stack = stacks[level]
            stack.append(root)
        else:
            stack = stacks[level]
            pre = stack.pop()
            pre.next = root
            stack.append(root)
        subtree_connect(root.left, level+1)
        subtree_connect(root.right, level+1)
    subtree_connect(root, 0)
