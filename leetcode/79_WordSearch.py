class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0]:
                    if self.dfs(board, word, i, j, {(i, j)}):
                        return True
        return False


    def dfs(self, board: List[List[str]], word: str, i: int, j: int, path: set[tuple[int, int]]) -> bool:
        if len(path) == len(word):
            return True

        index = len(path)
        m = range(len(board))
        n = range(len(board[i]))

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for x, y in directions:
            new_i = i + x
            new_j = j + y
            new_step = (new_i, new_j)
            if (new_i in m and new_j in n and
                board[new_i][new_j] == word[index] and
                new_step not in path):
                path.add(new_step)

                if self.dfs(board, word, new_i, new_j, path):
                    return True
                path.remove(new_step)
                
        return False
