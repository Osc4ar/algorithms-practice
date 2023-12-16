class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recursive(0, 0, m, n)

    def recursive(self, current_row: int, current_column: int, rows: int, cols: int):
        if current_row == rows or current_column == cols:
            return 0
        if current_row == rows - 1 and current_column == cols - 1:
            return 1

        return self.recursive(current_row + 1, current_column, rows, cols) + self.recursive(current_row, current_column + 1, rows, cols)