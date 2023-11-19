class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                node = (row, column)
                if (node not in visited and
                    grid[row][column] == "1"):
                    self.mapIsland(row, column, grid, visited)

                    count += 1

                visited.add(node)

        return count


    def mapIsland(self, row: int, column: int, grid: List[List[str]], visited: set[(int, int)]):
        next_nodes = deque()
        next_nodes.append((row, column))

        while len(next_nodes) > 0:
            current_row, current_column = next_nodes.popleft()
            next_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for direction in next_directions:
                new_row = current_row + direction[0]
                new_column = current_column + direction[1]
                new_node = (new_row, new_column)

                if (new_row in range(len(grid)) and
                    new_column in range(len(grid[0])) and
                    new_node not in visited and
                    grid[new_row][new_column] == "1"):
                    visited.add(new_node)
                    next_nodes.append(new_node)