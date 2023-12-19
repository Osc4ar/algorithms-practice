class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        previous_row = [0] * columns
        previous_row[columns - 1] = 1

        for row in reversed(range(rows)):
            for column in reversed(range(columns)):
                if obstacleGrid[row][column] == 1:
                    previous_row[column] = 0
                elif column + 1 < columns:
                    previous_row[column] = previous_row[column + 1] + previous_row[column]

        return previous_row[0]