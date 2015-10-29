# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/27'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        stack = [root]
        node = root
        record = []
        while stack:
            if node:
                record.append(str(node.val))
                stack.append(node)
                node = node.left
            else:
                record.append('E')
                t = stack.pop()
                node = t.right
        return ','.join(record)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        l = data.split(',')
        root = TreeNode(int(l[0]))
        parent = root
        stack = [parent]
        flag = 'left'
        for c in l[1:]:
            print c
            if c != 'E':
                t = TreeNode(int(c))
                if flag == 'left':
                    parent.left = t
                else:
                    parent = stack.pop()
                    parent.right = t
                    flag = 'left'
                parent = parent.left
                stack.append(t)
            else:
                if flag == 'left':
                    flag = 'right'
                else:
                    parent = stack.pop()
        return root


    def preorderTraversal(self, root):
        result = []
        def helper(root):
            if not root:
                result.append(None)
                return
            result.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(-1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(-2)
    # root.left.left.right = TreeNode(0)
    # root.left.right = TreeNode(3)
    c = Codec()
    a = c.serialize(root)
    print a
    b = c.deserialize(a)
    print c.preorderTraversal(b)

