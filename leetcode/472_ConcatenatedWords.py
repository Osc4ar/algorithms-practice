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

class Solution:
    '''
    Saving the strings on a set will make easier to find concatenated words
    Sorting the words by len will help us to discard words which are not concatenated, the smallers words are more likely to be part of
    longer words

    We can use a trie built for all the words, start building them from the shortest ones, the idea would be:
    1. If the word has a letter which has not leaf, we can discard it and just build a regular trie for it
    2. If the word has a letter with leaves, it might be a concatenated words.
    3. Iterate all the letter of the word in the existing trie, if the trie ends, check if the next letter has a new trie to traverse
    4. If it does not, then just build the trie as usual. If it does, continue the algorithm until the word ends
    5. If the word ends and it always had a node in a trie, add it to the results 
    '''
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_by_len = sorted(words, key=lambda s: len(s))
        trie = Trie()
        result = set()

        for word in words_by_len:
            if len(word) == 1:
                trie.insert(word)
                continue

            current = trie.root
            concatenated = True
            i = 0
            while i < len(word):
                c = word[i]
                if c not in current.children:
                    if '*' not in current.children:
                        concatenated = False
                        break
                    current = trie.root
                else:
                    current = current.children[c]
                    i += 1
            
            trie.insert(word)
            if concatenated:
                result.add(word)

        output = []
        for word in words:
            if word in result:
                output.append(word)

        return output
