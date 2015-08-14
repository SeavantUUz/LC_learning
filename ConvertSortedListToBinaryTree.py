# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/14'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)


def sortedListToBST(head):
    p = head
    l = []
    while p:
        l.append(p.val)
        p = p.next
    def sorted_array_to_bst(start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(l[mid])
        node.left = sorted_array_to_bst(start, mid-1)
        node.right = sorted_array_to_bst(mid+1, end)
        return node
    length = len(l)
    return sorted_array_to_bst(0, length-1)
