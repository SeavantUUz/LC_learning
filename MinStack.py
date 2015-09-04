# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/4'


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self._top = -1
        self._min = []
        self.min_value = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        self._top += 1
        if self.min_value > x:
            self.min_value = x
        self._min.append(self.min_value)

    def pop(self):
        """
        :rtype: nothing
        """
        _ = self.stack.pop()
        _ = self._min.pop()
        self._top -= 1
        if self._top == -1:
            self.min_value = float('inf')
        else:
            self.min_value = self._min[self._top]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self._top]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min[self._top]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(-10)
    stack.push(14)
    print stack.getMin()
    stack.push(-20)
    print stack.getMin()
    stack.pop()
    print stack._min
    stack.push(10)
    print stack._min
    print stack.getMin()
