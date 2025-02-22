class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        closest = defaultdict(set)
        for i, word in enumerate(wordList):
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                closest[pattern].add(word)
        
        queue = deque([beginWord])
        visited = set([beginWord])

        steps = 1
        while queue:
            steps += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nxt in closest[pattern]:
                        if nxt not in visited:
                            if nxt == endWord:
                                return steps
                            queue.append(nxt)
                            visited.add(nxt)

        return 0
