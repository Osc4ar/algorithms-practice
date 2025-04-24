class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        WATER = '0'
        ROWS = range(len(grid))
        COLS = range(len(grid[0]))

        count = 0
        visited = set()

        def bfs(start_row: int, start_col: int):
            queue = deque()
            queue.append((start_row, start_col))
            visited.add((start_row, start_col))

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()

                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                    for x, y in directions:
                        new_row = row + x
                        new_col = col + y
                        if (new_row in ROWS and
                            new_col in COLS and
                            grid[new_row][new_col] == LAND and
                            (new_row, new_col) not in visited):
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))

        for i in ROWS:
            for j in COLS:
                if grid[i][j] == LAND and (i,j) not in visited:
                    count += 1
                    bfs(i, j)

        return count
