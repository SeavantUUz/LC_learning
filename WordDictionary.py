# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/26'


# 之前维护的trie的代码fields为list, 维护了一套get和set方法，借鉴别人的代码，使用defaultdict来减少维护成本
from collections import defaultdict
class Node(object):
    def __init__(self):
        self.fields = defaultdict(Node)
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        node = self.root
        for ch in word:
            node = node.fields[ch]
        node.isWord = True

    def search(self, word):
        start = self.root
        self.res = False
        self._dfs(start, word)
        return self.res

    def _dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == '.':
            for n in node.fields.values():
                self._dfs(n, word[1:])
        else:
            t = node.fields.get(word[0])
            if not t:
                return
            self._dfs(t, word[1:])


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("word")
    print wordDictionary.search("pattern")
    print wordDictionary.search('.ord')
