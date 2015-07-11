# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/11'


def anagrams(strs):
    r_dict = dict()
    # duplicate_dict = dict()
    result = []
    for str_ in strs:
        # if not str_:
        #     continue
        # if duplicate_dict.get(str_):
        #     continue
        if not str_:
            key = ''
        else:
            key = tuple(sorted(list(str_)))
        # duplicate_dict[str_] = 1
        r_dict.setdefault(key, []).append(str_)
    for key in r_dict:
        if len(r_dict[key]) > 1:
            result.extend(r_dict[key])
    return result

if __name__ == '__main__':
    # print anagrams(['abc', 'cba', 'bca', 'dea', 'aed'])
    print anagrams([''])
