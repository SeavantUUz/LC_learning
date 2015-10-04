# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/5'


class Stack(object):
    from collections import deque
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = self.deque()
        self.top_num = None
        self.length = 0


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        self.length += 1
        self.top_num = x


    def pop(self):
        """
        :rtype: nothing
        """
        t_queue = self.deque()
        self.length -= 1
        t = None
        for i in xrange(self.length):
            t = self.queue.popleft()
            t_queue.append(t)
        self.queue = t_queue
        self.top_num = t



    def top(self):
        """
        :rtype: int
        """
        return self.top_num


    def empty(self):
        """
        :rtype: bool
        """
        return self.length == 0

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    print s.top()