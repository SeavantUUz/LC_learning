# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/19'


def isIsomorphic(s, t):
    s_dict = dict()
    t_dict = dict()
    for index, c in enumerate(s):
        s_dict.setdefault(c, []).append(index)
    for index, c in enumerate(t):
        t_dict.setdefault(c, []).append(index)
    return sorted(s_dict.values()) == sorted(t_dict.values())


if __name__ == '__main__':
    print isIsomorphic('egg', 'add')