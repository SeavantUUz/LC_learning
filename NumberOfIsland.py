# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/15'


def numIslands0(grid):
    if not grid:
        return
    from collections import deque
    n = len(grid)
    m = len(grid[0])
    queue = []
    count = 0
    def mark_it(x, y, grid):
        queue.append((x, y))
        while queue:
            x, y = queue.pop(0)
            grid[x][y] = '0'
            if x < n-1 and grid[x+1][y] == '1':
                queue.append((x+1, y))
            if y < m-1 and grid[x][y+1] == '1':
                queue.append((x, y+1))
    for i in xrange(n):
        for j in xrange(m):
            if grid[i][j] != '1':
                continue
            else:
                mark_it(i, j, grid)
                count += 1
    return count


# 他这个能过，我的不行，很奇怪，不知道主要的开销在哪里, 原因是超时
def numIslands(grid):
    grid=list([[int(j) for j in i] for i in grid])
    q=[]
    if not grid:
        return 0
    m,n=len(grid),len(grid[0])
    count=0
    for i in xrange(m):
        for j in xrange(n):
            if grid[i][j]!=1:
                continue
            count+=1
            q.append((i,j))
            grid[i][j]=2
            while q:
                x,y=q.pop(0)
                if x and grid[x-1][y]==1:
                    q.append((x-1,y))
                    grid[x-1][y]=2
                if y and grid[x][y-1]==1:
                    q.append((x,y-1))
                    grid[x][y-1]=2
                if x+1<m and grid[x+1][y]==1:
                    q.append((x+1,y))
                    grid[x+1][y]=2
                if y+1<n and grid[x][y+1]==1:
                    q.append((x,y+1))
                    grid[x][y+1]=2
    return count


if __name__ == '__main__':
    print numIslands0([list('11000'), list('11000'), list('00100'), list('00011')])
