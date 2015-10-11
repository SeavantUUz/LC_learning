# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/11'


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        t = []
        while self.stack:
            value = self.stack.pop()
            t.append(value)
        self.stack.append(x)
        while t:
            self.stack.append(t.pop())


    def pop(self):
        """
        :rtype: nothing
        """
        value = self.stack.pop()
        return value


    def peek(self):
        """
        :rtype: int
        """
        value = self.stack.pop()
        self.stack.append(value)
        return value


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    print queue.peek()
    print queue.pop()
    print queue.peek()
    print queue.pop()