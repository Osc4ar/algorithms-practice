class Solution:
    '''
    We have to do the iteration like this:
    1. From left to right, all columns
    2. From top to bottom, all rows except first one
    3. From right to left, all columns except first one
    4. From bottom to top, except first column
    5. From left to right, except last column
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        ROWS = len(matrix)
        COLS = len(matrix[0])
        target_size = ROWS * COLS

        start_row = 0
        start_col = 0
        while len(result) < target_size:
            for col in range(start_col, COLS):
                result.append(matrix[start_row][col])
            start_row += 1

            if len(result) == target_size:
                return result
    
            for row in range(start_row, ROWS):
                result.append(matrix[row][col])
            COLS -= 1
    
            if len(result) == target_size:
                return result
    
            for col in reversed(range(start_col, COLS)):
                result.append(matrix[row][col])
            ROWS -= 1

            if len(result) == target_size:
                return result
    
            for row in reversed(range(start_row, ROWS)):
                result.append(matrix[row][start_col])
            start_col += 1

        return result
