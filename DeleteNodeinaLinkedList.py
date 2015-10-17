# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/16'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        result = []
        tmp = self
        while tmp:
            result.append(tmp.val)
            tmp = tmp.next
        return '->'.join(map(str, result))

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        count = 0
        while next_node:
            count += 1
            print count
            node.val = next_node.val
            node = node.next
            next_node = next_node.next
        node.next = None


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    # l.next.next.next = ListNode(2)
    s = Solution()
    s.deleteNode(l)
