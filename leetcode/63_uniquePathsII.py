class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        previous_row = [0] * columns
        previous_row[columns - 1] = 1
        for row in reversed(range(rows)):
            current_row = [0] * columns
            
            for column in reversed(range(columns)):
                if obstacleGrid[row][column] == 1:
                    current_row[column] = 0
                elif column + 1 < columns:
                    current_row[column] = current_row[column + 1] + previous_row[column]
                else:
                    current_row[column] = previous_row[column]

            previous_row = current_row

        return previous_row[0]