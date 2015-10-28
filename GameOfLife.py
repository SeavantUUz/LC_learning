# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/28'

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        next_status = []
        for i in xrange(self.m):
            next_status.append([0]*self.n)
        for i in xrange(self.m):
            for j in xrange(self.n):
                next_status[i][j] = self.check(i, j, board)
        for i in xrange(self.m):
            for j in xrange(self.n):
                board[i][j] = next_status[i][j]

    def check(self, i, j, board):
        row = [i-1, i, i+1]
        col = [j-1, j, j+1]
        cur = board[i][j]
        # lives = sum([board[i][j] for i in row for j in col])
        lives = 0
        for x in row:
            for y in col:
                if x < 0 or x > self.m-1 or y < 0 or y > self.n-1:
                    continue
                else:
                    lives += board[x][y]
        live = lives - cur
        if cur:
            if live < 2:
                return 0
            elif live == 2 or live == 3:
                return cur
            else:
                return 0
        else:
            if live == 3:
                return 1
            else:
                return 0


