# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/24'


def findOrder(numCourses, prerequisites):
    result = []
    from collections import deque
    in_nodes = {i: set() for i in xrange(numCourses)}
    out_nodes = {i: set() for i in xrange(numCourses)}
    for i, j in prerequisites:
        in_nodes[i].add(j)
        out_nodes[j].add(i)
    queue = deque([node for node in in_nodes if len(in_nodes[node]) == 0])
    while queue:
        node = queue.popleft()
        result.append(node)
        for edge in out_nodes[node]:
            in_nodes[edge].remove(node)
            if len(in_nodes[edge]) == 0:
                queue.append(edge)
        in_nodes.pop(node)
    if in_nodes:
        return []
    else:
        return result


if __name__ == '__main__':
    # print findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print findOrder(4, [[0,1],[3,1],[1,3],[3,2]])


