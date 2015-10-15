# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/16'


# 第一种思路是遍历压栈，当等于其中一个时， 继续遍历，但是在遍历右边的时候，保存下root，然后判断是否找到另外一个
# 但是，这个方法虽然是O(n)理论最优，但是维护成本比较高，实现的代码比递归丑。并不符合优雅解法的定义。
# def lowestCommonAncestor(root, p, q):
#     stack = []
#     while root:
#         stack.append(root)
#         root = root.left
#     while stack:
#         node = stack.pop()

# 这个最直观，但是我不知道复杂度，看讨论似乎也是O(n)，但我总觉得有重复计算
# 这玩意绝对不是O(n)
# 玄幻的事情发生了……
# 用闭包的，TLE……
# 用类的，beating 100%....
def lowestCommonAncestor(root, p, q):
    def is_descendant(x, y):
        if not x:
            return False
        elif x == y:
            return True
        else:
            return is_descendant(x.left, y) or is_descendant(x.right, y)
    if not root:
        return
    if is_descendant(root.left, p) and is_descendant(root.right, q) or is_descendant(root.left, q) and \
            is_descendant(root.right, p):
        return root
    else:
        return lowestCommonAncestor(root.left, p, q) or lowestCommonAncestor(root.right, p, q)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if self.isDescendantOf(p, q):
            return p
        if self.isDescendantOf(q, p):
            return q

        if self.isDescendantOf(root.left, p) and self.isDescendantOf(root.right, q) or self.isDescendantOf(root.left, q) and self.isDescendantOf(root.right, p):
            return root
        else:
            return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)




    def isDescendantOf(self, x, y):
        """
        Check if y is a descendant of x
        """
        if x is None:
            return False
        if x == y:
            return True
        else:
            return self.isDescendantOf(x.right, y) or self.isDescendantOf(x.left, y)
