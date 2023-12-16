class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        previous_row = [1] * n

        for row in range(m - 2, -1, -1):
            current_row = [0] * n
            current_row[n - 1] = 1

            for col in range(n - 2, -1, -1):
                current_row[col] = current_row[col + 1] + previous_row[col]

            previous_row = current_row

        return previous_row[0]