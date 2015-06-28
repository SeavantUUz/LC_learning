# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/26'

def kmp(haystack, needle):
    def search(source, target):
        M = len(source)
        N = len(target)
        i = j = 0
        while i < M and j < N:
            j = dfa[ord(source[i])][j]
            i += 1
        if j == N:
            return i - N
        else:
            return -1
    def build_dfa(source, target):
        dfa = dict()
        N = len(target)
        # init dfa
        for i in range(256):
            dfa[i] = dict()
            for j in range(N):
                dfa[i][j] = 0
        X = 0
        j = 1
        dfa[ord(target[0])][0] = 1
        while j < N:
            for key in dfa:
                dfa[key][j] = dfa[key][X]
            ascii = ord(target[j])
            dfa[ascii][j] = j+1
            X = dfa[ascii][X]
            j+=1
        return dfa
    if not haystack:
        return -1
    if not needle:
        return -1
    dfa = build_dfa(haystack, needle)
    return search(haystack, needle)


if __name__ == "__main__":
    source = 'bcbaabacaababacaa'
    target = 'cba'
    print kmp(source, target)
