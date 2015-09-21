# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/21'


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


def reverseList(head):
    v_head = ListNode(None)
    pre, cur = v_head, head
    while cur:
        q = cur.next
        cur.next = v_head.next
        v_head.next = cur
        cur = q
    return v_head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)
    # l1.next.next.next.next = ListNode(5)
    print reverseList(l1)