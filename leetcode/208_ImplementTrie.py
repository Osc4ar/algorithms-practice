class Node:
    def __init__(self, val: str):
        self.val = val
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node('*')

    def insert(self, word: str) -> None:
        trie = self.root

        for c in word:
            if c not in trie.children:
                child = Node(c)
                trie.children[c] = child
                trie = child
            else:
                trie = trie.children[c]
        
        trie.children['*'] = None

    def search(self, word: str) -> bool:
        trie = self.root

        for c in word:
            if c not in trie.children:
                return False
            trie = trie.children[c]

        return '*' in trie.children

    def startsWith(self, prefix: str) -> bool:
        trie = self.root

        for c in prefix:
            if c not in trie.children:
                return False
            trie = trie.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
