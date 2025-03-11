class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                concatenated = (prefix in words_set and suffix in words_set) or (prefix in words_set and dfs(suffix))
                if concatenated:
                    dp[word] = True
                    return True
            dp[word] = False
            return False

        result = []
        for word in words:
            if dfs(word):
                result.append(word)
        return result
