class Solution:
    '''
    If it is possible to transform the word, we will have (2 + different letter) steps as the result
    We cannot assume if we have the end word we have the needed middle words.
    We can return 0 directly if the target word is not in the wordList, to check if a given word is on the list
    we can convert it to a set

    We could group the words which are 1 letter distance of each other, the key would be the initial word and
    the values a list of similar words. We could start at the words closer to our word by 1 and then do BFS until
    we find the endword.

    We also need to identify how many letters to change, if we can keep some letters we can skip similar words which change
    unwanted letters

    ["hot","dot","dog","lot","log","cog"]
    {
        'hot': ['dot', 'lot'],
        'dot': ['dog', 'hot', 'lot'],
        'dog': ['cog', 'dot', 'log'],
        'lot': ['log'],
        'log': ['cog', 'dog', 'log'],
        'cog': ['dog', 'log']
    }
    hit
    [hot]
    [dot, lot]
    [dog, hot, lot, log]
    [cog]

    0. Build the hash map containing closest words
    1. We can check start by all the words closer to hit
    2. Then we use BFS to visit all the words closer to the current word, we can avoid duplicates/cycles by
    3. Keeping a list of visited nodes
    4. We continue until we reach the end word or we have not further options in queue, if we did not find the word we return 0
    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList):
            return 0

        closest = defaultdict(set)
        for i, w1 in enumerate(wordList):
            for j in range(i, len(wordList)):
                w2 = wordList[j]
                if w2 not in closest[w1]:
                    d = self.diff(w1, w2)
                    if d == 1:
                        closest[w1].add(w2)
                        closest[w2].add(w1)
        
        queue = deque()
        visited = set()
        for w in wordList:
            if self.diff(beginWord, w) == 1:
                if w == endWord:
                    return 2
                queue.append(w)
                visited.add(w)

        steps = 2
        while queue:
            steps += 1
            for _ in range(len(queue)):
                w = queue.popleft()
                for nxt in closest[w]:
                    if nxt == endWord:
                        return steps
                    if nxt not in visited:
                        queue.append(nxt)
                        visited.add(nxt)

        return 0

    def diff(self, w1: str, w2: str) -> int:
        diffs = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diffs += 1
        return diffs
