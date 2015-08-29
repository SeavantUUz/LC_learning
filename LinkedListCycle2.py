# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/29'


def detectCycle0(head):
    slow_count = 0
    fast_count = 1
    if not head or not head.next:
        return None
    s_p = head
    f_p = head.next
    while f_p and f_p.next:
        if s_p == f_p:
            break
        else:
            s_p= s_p.next
            slow_count += 1
            f_p = f_p.next.next
            fast_count += 2
    else:
        return None
    cycle_count = f_p - s_p
    s_p = head
    for i in xrange(slow_count):
        f_p = s_p
        count = cycle_count
        while count:
            f_p = f_p.next
            count -= 1
        if s_p == f_p:
            return s_p
        else:
            s_p = s_p.next
    return s_p


def detectCycle(head):
    if not head or not head.next:
        return None
    s_p = head
    f_p = head.next
    while f_p and f_p.next:
        if s_p == f_p:
            break
        else:
            s_p= s_p.next
            f_p = f_p.next.next
    else:
        return None
    p = head
    s_p = s_p.next
    while p != s_p:
        p = p.next
        s_p = s_p.next
    return p