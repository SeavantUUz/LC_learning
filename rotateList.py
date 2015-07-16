# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/16'


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


def rotateRight(head, k):
    if head is None:
        return None
    if head.next is None:
        return head
    p = head
    count = 1
    while p.next:
        count += 1
        p = p.next
    tail = p
    r_k = count - k
    p = head
    if r_k == 0:
        return head
    elif r_k < 0:
        new_head = None
        while p:
            q = p
            p = p.next
            q.next = new_head
            new_head = q
        return new_head
    else:
        index = 1
        while index < r_k:
            p = p.next
            index += 1
        tail.next = head
        head = p.next
        p.next = None
        return head


## 别人的解法，学着点！

def rotateRight(head, k):
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        while fast and fast.next:
            fast = fast.next
            length += 1

        k %= length
        fast = head

        while k:
            fast = fast.next
            k -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    print rotateRight(l1, 2)




