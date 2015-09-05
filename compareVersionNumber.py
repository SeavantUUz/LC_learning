# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/5'


def compareVersion0(version1, version2):
    version1_list = version1.split('.')
    version2_list = version2.split('.')
    length1 = len(version1_list)
    length2 = len(version2_list)
    min_length = min([length1, length2])
    index = 0
    while index < min_length:
        version1_current = version1_list[index]
        version2_current = version2_list[index]
        if index == 0:
            version1_current = int(version1_current)
            version2_current = int(version2_current)
        else:
            len1 = len(version1_current)
            len2 = len(version2_current)
            delta = abs(len1-len2)
            version1_current = int(version1_current)
            version2_current = int(version2_current)
            if len1 > len2:
                version2 *= delta * 10
            else:
                version1 *= delta * 10
        if version1_current > version2_current:
            return 1
        elif version1_current < version2_current:
            return -1
        else:
            index += 1
    else:
        if length1 == length2:
            return 0
        elif length1 > length2:
            return 1
        else:
            return -1

def compareVersion(version1, version2):
    v1 = [int(item) for item in version1.split('.')]
    v2 = [int(item) for item in version2.split('.')]
    lv1 = len(v1)
    lv2 = len(v2)
    if lv1 > lv2:
        v2 += [0] * (lv1-lv2)
    else:
        v1 += [0] * (lv2-lv1)
    if v1 == v2:
        return 0
    elif v1 < v2:
        return -1
    else:
        return 1



if __name__ == '__main__':
    print compareVersion('0.1', '1.1')
    print compareVersion('01', '1')
    print compareVersion('1.2', '1.10')
    # 看来我意思没理解对，我认为这个应该返回-1的，但是应该不会写成这样，而应该是1.0.2
    print compareVersion('1.02', '1.1')
