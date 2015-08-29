# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/29'

def linked_list_cycle(head):
    if not head or not head.next:
        return False
    slow_pointer = head
    fast_pointer = head.next
    while fast_pointer and fast_pointer.next:
        if slow_pointer == fast_pointer:
            break
        else:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
    else:
        return False
    return True


if __name__ == '__main__':

