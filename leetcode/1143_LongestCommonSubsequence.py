class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for row in reversed(range(len(text1))):
            for column in reversed(range(len(text2))):
                if text1[row] == text2[column]:
                    dp[row][column] = 1 + dp[row + 1][column + 1]
                else:
                    dp[row][column] = max(dp[row][column + 1], dp[row + 1][column])

        return dp[0][0]