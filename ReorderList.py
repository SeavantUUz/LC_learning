# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/30'

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

def reorderList(head):
    if not head:
        return None
    length = 1
    v_head = ListNode(head.val)
    current = head.next
    while current:
        t = ListNode(current.val)
        current = current.next
        t.next = v_head
        v_head = t
        length += 1
    index = 0
    nv_head = ListNode(None)
    n_head = nv_head
    while index < length / 2:
        p = head
        head = head.next
        p.next = None
        q = v_head
        v_head = v_head.next
        q.next = None
        n_head.next = p
        n_head = n_head.next
        n_head.next = q
        n_head = n_head.next
        index += 1
    if length % 2:
        t = head
        t.next = None
        n_head.next = t
    return nv_head.next



if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    print reorderList(l1)


