# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/6/26'

def kmp0(haystack, needle):
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


def kmp(haystack, needle):
    def search(source, target):
        M = len(source)
        N = len(target)
        i = 0
        o = 0
        while i < M:
            j = 0
            # dfa success advance
            while i+j < M and j<N and source[i+j] == target[j]:
                j += 1
            # match
            if j == N:
                return i
            o = over[j]
            i = i+max(1, j-o)
        return -1
    def overlap(target):
        over = dict()
        N = len(target)
        over[0] = 0
        for o in xrange(N):
            i = 0
            j=o
            count = 0
            while i< N and j>=0 and i<j:
                if target[i] == target[j]:
                    count += 2
                    i+=1
                    j-=1
                else:
                    break
            else:
                if j%2:
                    count += 1
            over[o] = count
        return over
    over = overlap(needle)
    return search(haystack, needle)


def kmp2(haystack, needle):
    def search(source, target):
        M = len(source)
        N = len(target)
        i = 0
        o = 0
        while i < M:
            j = 0
            # dfa success advance
            while i+j < M and j<N and source[i+j] == target[j]:
                j += 1
            # match
            if j == N:
                return i
            o = over[j]
            i = i+max(1, j-o)
        return -1
    def overlap(target):
        over = dict()
        N = len(target)
        i = 0
        over[0] = -1
        while i<N:
            over[i+1] = over[i] + 1
            while over[i+1] > 0 and target[i] != target[over[i+1]-1]:
                over[i+1] = over[over[i+1]-1]+1
            i+=1
        return over
    over = overlap(needle)
    return search(haystack, needle)


if __name__ == "__main__":
    source = 'babbbbb'
    target = 'ccc'
    print kmp(source, target)
