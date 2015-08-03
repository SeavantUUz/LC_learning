# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/4'


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


def reverseBetween(head, m, n):
    p = head
    n_head = None
    n_tail = None
    index = 1
    dummy = ListNode(0)
    presudo_p = dummy
    presudo_p.next = p
    while index < m:
        presudo_p = presudo_p.next
        index += 1
    if index == 1:
        flag = 1
    else:
        flag = 0
    p = presudo_p
    q = p.next
    while index <= n:
        if not n_head:
            n_tail = q
            n_head = q
            q = q.next
            n_tail.next = None
        else:
            pp = q.next
            q.next = n_head
            n_head = q
            q = pp
        index += 1
    n_tail.next = q
    p.next = n_head
    if flag:
        return n_head
    else:
        return head


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    print reverseBetween(a, 3, 3)



