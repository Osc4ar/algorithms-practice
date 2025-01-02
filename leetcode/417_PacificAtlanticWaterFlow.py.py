class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        ROWS = range(len(heights))
        COLS = range(len(heights[0]))

        def dfs(row: int, col: int, lastHeight: int, ocean: set[tuple[int]]):
            if ((row, col) in ocean or
                row not in ROWS or
                col not in COLS or
                heights[row][col] < lastHeight):
                return

            ocean.add((row, col))
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for x, y in directions:
                dfs(row + x, col + y, heights[row][col], ocean)

        for c in COLS:
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS[-1], c, heights[ROWS[-1]][c], atlantic)

        for r in ROWS:
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS[-1], heights[r][COLS[-1]], atlantic)

        return list(pacific & atlantic)
