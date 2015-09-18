# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/18'

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


def removeElements(head, val):
    if not head:
        return None
    v_head = ListNode(None)
    pre, cur = None, head
    while cur:
        if cur.val == val:
            cur = cur.next
        else:
            if not pre:
                v_head.next = cur
                pre = cur
                cur = cur.next
                pre.next = None
            else:
                pre.next = cur
                cur = cur.next
                pre = pre.next
                pre.next = None
    return v_head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next =ListNode(2)
    head.next.next =ListNode(2)
    head.next.next.next =ListNode(1)
    print removeElements(head, 1)



