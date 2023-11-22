class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = deque()

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    fresh.add((row, column))
                elif grid[row][column] == 2:
                    rotten.append((row, column))

        minutes = self.expandRottenOranges(grid, fresh, rotten)
        
        if len(fresh) > 0:
            return -1

        return minutes

    def expandRottenOranges(self, grid: List[List[int]], fresh: set[(int, int)], rotten) -> int:
        minutes = 0

        while rotten:
            increase_count = 0
            for _ in range(len(rotten)):
                current_row, current_column = rotten.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for direction in directions:
                    new_row = current_row + direction[0]
                    new_column = current_column + direction[1]

                    if (new_row in range(len(grid)) and
                        new_column in range(len(grid[0])) and
                        grid[new_row][new_column] == 1):
                        rotten.append((new_row, new_column))
                        grid[new_row][new_column] = 2
                        increase_count = 1
                        fresh.remove((new_row, new_column))

            minutes += increase_count

        return minutes
                        