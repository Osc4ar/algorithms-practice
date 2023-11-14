class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.countIslands(grid, 0, 0, set(), set())

    def countIslands(self, grid: List[List[str]], row: int, column: int, visited: set[tuple[int, int]], counted: set[tuple[int, int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        if min(row, column) < 0 or row >= ROWS or column >= COLUMNS or (row, column) in visited:
            return 0

        count = 0
        visited.add((row, column))

        if grid[row][column] == '1':
            if not self.islandAlreadyCounted(row, column, counted):
                print(f'added to count ({row}, {column})')
                count += 1

            counted.add((row, column))
            print(counted)

        count += self.countIslands(grid, row + 1, column, visited, counted)
        count += self.countIslands(grid, row - 1, column, visited, counted)
        count += self.countIslands(grid, row, column + 1, visited, counted)
        count += self.countIslands(grid, row, column - 1, visited, counted)

        return count

    def islandAlreadyCounted(self, row: int, column: int, island: set[tuple[int, int]]) -> bool:
        if (row + 1, column) in island:
            return True
        if (row - 1, column) in island:
            return True
        if (row, column + 1) in island:
            return True
        if (row, column - 1) in island:
            return True
        
        return False