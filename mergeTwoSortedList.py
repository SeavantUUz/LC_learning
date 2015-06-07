# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/5'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = []
        tmp = self
        while tmp:
            result.append(tmp.val)
            tmp = tmp.next
        return result.__str__()

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
            return result
        else:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)
            return result
        return result


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(5)
    b = ListNode(2)
    b.next = ListNode(3)
    # print mergeTwoLists(a, b)
