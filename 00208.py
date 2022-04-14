class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isWord = False



class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        if not word:
            return

        node = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not node.child[index]:
                node.child[index] = TrieNode()
            node = node.child[index]
        node.isWord = True

    def search(self, word: str) -> bool:
        if not word:
            return False

        node = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not node.child[index]:
                return False
            node = node.child[index]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False

        node = self.root
        for w in prefix:
            index = ord(w) - ord('a')
            if not node.child[index]:
                return False
            node = node.child[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
