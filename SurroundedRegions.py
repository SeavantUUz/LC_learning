# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/23'

from collections import deque

def surroundedRegions(board):
    if not board:
        return
    n = len(board)
    m = len(board[0])
    def mark_it(x, y, board):
        queue = deque()
        if board[x][y] == 'O':
            queue.append((x, y))
            board[x][y] = 'P'
        while queue:
            x, y = queue.popleft()
            if x > 0 and board[x-1][y] == 'O':
                queue.append((x-1, y))
                board[x-1][y] = 'P'
            if x < n-1 and board[x+1][y] == 'O':
                queue.append((x+1, y))
                board[x+1][y] = 'P'
            if y > 0 and board[x][y-1] == 'O':
                queue.append((x, y-1))
                board[x][y-1] = 'P'
            if y < m-1 and board[x][y+1] == 'O':
                queue.append((x, y+1))
                board[x][y+1] = 'P'
    for i in range(m):
        mark_it(0, i, board)
        mark_it(n-1, i, board)
    for j in range(n):
        mark_it(j, 0, board)
        mark_it(j, m-1, board)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'P':
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'
    print board

if __name__ == '__main__':
    # a = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    # a = [list('OO'), list('OO')]
    a = [list("XOXOXO"),list("OXOXOX"),list("XOXOXO"),list("OXOXOX")]
    surroundedRegions(a)



