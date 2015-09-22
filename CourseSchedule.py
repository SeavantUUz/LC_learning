# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/22'


# 拓扑排序，算法是抄的
def canFinish(numCourses, prerequisites):
    from collections import deque
    in_edges = {i: set() for i in xrange(numCourses)}
    out_edges = {i: set() for i in xrange(numCourses)}
    for _in, _out in prerequisites:
        in_edges[_in].add(_out)
        out_edges[_out].add(_in)
    # 入度为0
    queue = deque([node for node in in_edges if len(in_edges[node]) == 0])
    while queue:
        node = queue.popleft()
        for edge in out_edges[node]:
            in_edges[edge].remove(node)
            if len(in_edges[edge]) == 0:
                queue.append(edge)
        in_edges.pop(node)
    return not in_edges


if __name__ == '__main__':
    print canFinish(2, [[1,0],[0,1]])
