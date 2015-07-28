# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/29'


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


def deleteDuplicate(head):
    if not head:
        return head
    p = head
    pre = head.val
    q = head.next
    while q:
        if q.val != pre:
            pre = q.val
            p.next = q
            q = q.next
            p = p.next
        else:
            p.next = None
            q = q.next
    return head


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(2)
    print deleteDuplicate(l)

