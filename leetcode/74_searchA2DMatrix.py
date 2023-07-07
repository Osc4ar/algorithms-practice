class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        matrix_size = rows * cols

        left = 0
        right = matrix_size - 1
        while left <= right:
            middle = (right + left) // 2

            (i, j) = self.convert_to_matrix_indexes(middle, cols)
            if target < matrix[i][j]:
                right = middle - 1
            elif target > matrix[i][j]:
                left = middle + 1
            else:
                return True

        return False

    def convert_to_matrix_indexes(self, index, cols):
        return (index // cols, index % cols)
        