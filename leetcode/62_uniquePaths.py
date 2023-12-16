class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        return self.recursive(cache, 0, 0, m, n)

    def recursive(self, cache: list[list[int]], current_row: int, current_column: int, rows: int, cols: int):
        if current_row == rows or current_column == cols:
            return 0
        if cache[current_row][current_column] > 0:
            return cache[current_row][current_column]
        if current_row == rows - 1 and current_column == cols - 1:
            return 1

        cache[current_row][current_column] = self.recursive(cache, current_row + 1, current_column, rows, cols) + self.recursive(cache, current_row, current_column + 1, rows, cols)

        return cache[current_row][current_column]