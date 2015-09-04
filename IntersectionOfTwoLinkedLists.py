# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/5'


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
        return '->'.join(map(str, result))


def getIntersectionNode(headA, headB):
    def Length(head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count
    if not headA or not headB:
        return None
    lengthA = 1+Length(headA.next)
    lengthB = 1+Length(headB.next)
    if lengthA > lengthB:
        delta = lengthA - lengthB
        while delta > 0:
            headA = headA.next
            delta -= 1
    if lengthA < lengthB:
        delta = lengthB - lengthA
        while delta > 0:
            headB = headB.next
            delta -= 1
    while headA and headB:
        if headA == headB:
            return headA
        else:
            headA = headA.next
            headB = headB.next
    else:
        return None


