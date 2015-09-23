# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/9/24'

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fields = []

    def set(self, ch):
        self.ch = ch

    def put(self, ch):
        for node in self.fields:
            if node.ch == ch:
                return node
        else:
            node = TrieNode()
            node.set(ch)
            self.fields.append(node)
            return node

    def get(self, ch):
        for node in self.fields:
            if node.ch == ch:
                return node
        else:
            return None


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            cur = node.put(ch)
            node = cur
        node.put('')


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            cur = node.get(ch)
            if cur is None:
                break
            node = cur
        else:
            if node.get(''):
                return True
            else:
                return False
        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            cur = node.get(ch)
            if cur is None:
                break
            node = cur
        else:
            return True
        return False


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("abc")
print trie.search("abc")
print trie.search("ab")
trie.insert("ab")
print trie.search("ab")
trie.insert("ab")
print trie.search("ab")
