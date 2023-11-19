class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_island_size = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                node = (row, column)

                if node not in visited and grid[row][column] == 1:
                    visited.add(node)
                    island_size = self.measureIslandSize(row, column, grid, visited)
                    if island_size > max_island_size:
                        max_island_size = island_size
                else:
                    visited.add(node)

        return max_island_size

    def measureIslandSize(self, row: int, column: int, grid: List[List[int]], visited: set[(int, int)]) -> int:
        next_nodes = deque([(row, column)])
        island_size = 1
        print(f'Root: {row}, {column}')

        while len(next_nodes) > 0:
            current_row, current_column = next_nodes.popleft()
            current_node = (current_row, current_column)

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for direction in directions:
                new_row = current_row + direction[0]
                new_column = current_column + direction[1]
                new_node = (new_row, new_column)

                if (new_row in range(len(grid)) and
                    new_column in range(len(grid[0])) and
                    new_node not in visited and
                    grid[new_row][new_column] == 1):
                    next_nodes.append(new_node)
                    visited.add(new_node)
                    island_size += 1
                    print(new_node)
        
        return island_size
