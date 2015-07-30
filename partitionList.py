# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/31'


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


def partition(head, x):
    dummy= ListNode(0)
    dummy_g = ListNode(0)
    dummy_less_head = dummy
    dummy_greater_head = dummy_g
    if not head:
        return head
    p = head
    while p:
        if p.val >= x:
            dummy_greater_head.next = p
            dummy_greater_head = p
        else:
            dummy_less_head.next = p
            dummy_less_head = p
        p = p.next
    dummy_greater_head.next = None
    dummy_less_head.next = dummy_g.next
    return dummy.next


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(4)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(5)
    l.next.next.next.next.next = ListNode(2)
    print partition(l, 3)
