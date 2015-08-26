# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/26'


def canCompleteCircuit(gas, cost):
    r = 0
    sum = 0
    cur = 0
    for index in xrange(len(gas)):
        sum += gas[index] - cost[index]
        cur += gas[index] - cost[index]
        if cur < 0:
            cur = 0
            r = index + 1
    if sum < 0:
        return -1
    return r


if __name__ == '__main__':
    # print canCompleteCircuit([5], [4])
    print canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
