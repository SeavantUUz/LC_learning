# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/1'

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

def sortList(head):
    if not head:
        return None
    values = []
    p = head.next
    values.append(head.val)
    while p:
        values.append(p.val)
        p = p.next
    values.sort()
    head.val = values[0]
    p = head.next
    index = 1
    while p:
        p.val = values[index]
        p = p.next
        index += 1
    return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(5)
    l1.next.next.next.next = ListNode(4)
    print sortList(l1)