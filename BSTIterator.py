# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/10'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return "node: {}".format(self.val)


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return False
        else:
            return True


    def next(self):
        """
        :rtype: int
        """
        current = self.stack.pop()
        root = current.right
        while root:
            self.stack.append(root)
            root = root.left
        return current.val


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    t, v = BSTIterator(root), []
    while t.hasNext():
        v.append(t.next())
    print v