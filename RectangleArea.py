# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/4'


def computeArea(A, B, C, D, E, F, G, H):
    first_area = (C-A) * (D-B)
    second_area = (G-E) * (H-F)
    total_area = first_area + second_area
    overlap = max((min(C, G) - max(A, E)), 0) * max((min(D, H) - max(B, F)), 0)
    return total_area - overlap