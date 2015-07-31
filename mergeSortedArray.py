# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/8/1'


def merge0(nums1, m, nums2, n):
    m_index = m
    n_index = n
    if m == 0:
        nums1 = nums2
        return
    while m_index and n_index:
        if nums2[n_index-1] >= nums1[m_index-1]:
            nums1.insert(m_index, nums2[n_index-1])
            n_index -= 1
        else:
            m_index -= 1
    if n_index:
        while n_index:
            nums1.insert(0, nums2[n_index-1])
            n_index -= 1


def merge(nums1, m, nums2, n):
    m_index = m-1
    n_index = n-1
    index = m+n-1
    while m_index>=0 and n_index>=0:
        if nums1[m_index] >= nums2[n_index]:
            nums1[index] = nums1[m_index]
            m_index -= 1
        else:
            nums1[index] = nums2[n_index]
            n_index -= 1
        index -= 1
    if m_index < 0:
        nums1[:n_index+1] = nums2[:n_index+1]
    print nums1


if __name__ == '__main__':
    merge([1,3,4,5], 1, [2,3,4, 6, 7, 8], 2)