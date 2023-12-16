class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        cache = [[0] * columns for _ in range(rows)]
        return self.recursive(obstacleGrid, 0, 0, cache)

    def recursive(self, obstacleGrid: List[List[int]], row: int, column: int, cache: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        if row == rows or column == columns:
            return 0
        if obstacleGrid[row][column] == 1:
            return 0
        if row == rows - 1 and column == columns - 1 and obstacleGrid[row][column] != 1:
            return 1

        if cache[row][column] > 0:
            return cache[row][column]

        cache[row][column] = self.recursive(obstacleGrid, row + 1, column, cache) + self.recursive(obstacleGrid, row, column + 1, cache)
        return cache[row][column]
