class Trie(object):

    # 字典树
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
    # insert 'apple' ---> {u'a': {u'p': {u'p': {u'l': {u'e': {'end': u'apple'}}}}}} 
    # insert 'app' ----> {u'a': {u'p': {u'p': {'end': u'app', u'l': {u'e': {'end': u'apple'}}}}}}
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.trie
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['end'] = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.trie
        for c in word:
            if c not in root:
                return False
            root = root[c]
        return "end" in root

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.trie
        # print root
        for c in prefix:
            if c not in root:
                return False
            root = root[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
