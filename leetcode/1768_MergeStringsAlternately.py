class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i == len(word1):
                result.append(word2[j])
                j += 1
            elif j == len(word2):
                result.append(word1[i])
                i += 1
            elif j < i:
                result.append(word2[j])
                j += 1
            else:
                result.append(word1[i])
                i += 1

        return ''.join(result)
