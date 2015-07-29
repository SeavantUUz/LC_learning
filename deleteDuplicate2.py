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


def deleteDuplicates0(head):
    if not head:
        return head
    pre = head
    cur = pre.next
    if not cur:
        return head
    pos = cur.next
    if not pos:
        if pre.val == cur.val:
            return None
        else:
            return head
    add_flag = True
    while cur and pos:
        if cur.val == pos.val:
            add_flag = False
            pos = pos.next
        else:
            if add_flag:
                pre.next = cur
                cur = cur.next
                pos = pos.next
                pre = pre.next
            else:
                add_flag = True
                cur = pos
                pos = pos.next
    if add_flag:
        pre.next = cur
    return head


def deleteDuplicates(head):
    # 这个方法赞！
    dummy = ListNode(0)
    prev, current = dummy, head
    while current:
        next = current.next
        if not next or next.val != current.val:
            prev.next = current
            prev = prev.next
        else:
            while next and next.val == current.val:
                next = next.next
            prev.next = next
        current = next
    return dummy.next



if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    # l.next.next.next = ListNode(2)
    print deleteDuplicates(l)


