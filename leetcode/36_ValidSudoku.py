class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets = [set() for _ in range(9)]
        # 3x3 matrix of sets
        blocks = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(len(board)):
            row_set = set()
            for col in range(len(board[row])):
                cell = board[row][col]
                block = blocks[row // 3][col // 3]
                col_set = col_sets[col]

                if cell == '.':
                    continue
                if cell in row_set:
                    return False
                if cell in block:
                    return False
                if cell in col_set:
                    return False

                row_set.add(cell)
                col_set.add(cell)
                block.add(cell)

        return True
