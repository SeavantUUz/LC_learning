# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/13'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)


def sortedArrayToBST(nums):
    def build_tree(start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        node.left = build_tree(start, mid-1)
        node.right = build_tree(mid+1, end)
        return node
    length = len(nums)
    root = build_tree(0, length-1)
    return root


if __name__ == '__main__':
    print sortedArrayToBST([1,2,4,5,6])



