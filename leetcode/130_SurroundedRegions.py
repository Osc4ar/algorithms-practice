class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        ROWS = range(len(board))
        COLS = range(len(board[0]))

        def dfs(row: int, col: int):
            visited.add((row, col))

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in directions:
                if (row + x in ROWS and
                    col + y in COLS and
                    board[row + x][col + y] == 'O' and
                    (row + x, col + y) not in visited):
                    dfs(row + x, col + y)

        for c in COLS:
            if board[0][c] == 'O' and (0, c) not in visited:
                dfs(0, c)
            if board[ROWS[-1]][c]== 'O' and (ROWS[-1], c) not in visited:
                dfs(ROWS[-1], c)

        for r in ROWS:
            if board[r][0] == 'O' and (r, 0) not in visited:
                dfs(r, 0)
            if board[r][COLS[-1]] == 'O' and (r, COLS[-1]) not in visited:
                dfs(r, COLS[-1])

        for r in ROWS:
            for c in COLS:
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
