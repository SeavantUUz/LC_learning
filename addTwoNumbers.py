# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/7'

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


def addTwoNumbers(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    def addTwoNumbersRec(l1, l2, c):
        if l1 is None and l2 is None and not c:
            return None
        elif l1 is None and l2 is None and c:
            x = c
        elif l1 and l2:
            x = l1.val + l2.val + c
            l1 = l1.next
            l2 = l2.next
        elif l1:
            x = l1.val + c
            l1 = l1.next
        else:
            print l2
            x = l2.val + c
            l2 = l2.next
        a = x % 10
        c = x / 10
        result = ListNode(a)
        result.next = addTwoNumbersRec(l1, l2, c)
        return result
    return addTwoNumbersRec(l1, l2, 0)


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(9)
    l2.next = ListNode(5)
    print addTwoNumbers(l1, l2)
