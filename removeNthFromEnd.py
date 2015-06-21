# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/21'

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

def removeNthFromEnd0(head, n):
    p = head
    n_head = None
    while p:
        q = p
        p = p.next
        q.next = n_head
        n_head = q
    count = 0
    while n_head:
        if count + 1 == n:
            r_node = n_head.next
            if r_node:
                n_head.next = r_node.next
            else:
                n_head.next = None
        else:
            n_head = n_head.next
    return head


def removeNthFromEnd(head, n):
    p = head
    length = 0
    while p:
        p = p.next
        length += 1
    n_n = length - n
    if n_n < 0:
        return head
    elif n_n == 0:
        return head.next
    else:
        count = 0
        p = head
        while p:
            if count+1 == n_n:
                r_node = p.next
                if r_node:
                    p.next = r_node.next
                    p = p.next
                    count += 1
                else:
                    p.next=None
            else:
                p = p.next
                count += 1
        return head



if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)
    # l1.next.next.next.next = ListNode(5)
    print removeNthFromEnd(l1, 1)

