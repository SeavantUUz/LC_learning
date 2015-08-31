# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/31'


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


def insertionSortList(head):
    v_head = ListNode(None)
    while head:
        q = head
        head = head.next
        q.next = None
        p = v_head.next
        pre = None
        while p:
            if p.val < q.val:
                pre = p
                p = p.next
            else:
                if not pre:
                    q.next = p
                    v_head.next = q
                else:
                    q.next = p
                    pre.next = q
                break
        else:
            if not pre:
                v_head.next = q
            else:
                pre.next = q
    return v_head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    # l1.next.next = ListNode(2)
    # l1.next.next.next = ListNode(5)
    # l1.next.next.next.next = ListNode(4)
    print insertionSortList(l1)


