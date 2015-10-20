# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/19'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if not root:
            return []
        else:
            self.helper(root, [])
        return self.result


    def helper(self, root, one_path):
        if not root:
            return
        one_path.append(str(root.val))
        if not root.left and not root.right:
            self.result.append('->'.join(one_path))
        else:
            self.helper(root.left, one_path[:])
            self.helper(root.right, one_path[:])


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print s.binaryTreePaths(root)
