# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/24'


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


def swapPairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    pre, p, q = None, head, head.next
    head = head.next
    while p and q:
        p.next = q.next
        if pre:
            pre.next = q
        pre = p
        p = q.next
        q.next = pre
        if p:
            q = p.next
        else:
            q = None
    return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(6)
    print swapPairs(l1)
