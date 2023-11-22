class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        if grid[0][0] == 1:
            return -1

        visited = set()
        visited.add((0, 0))

        next_nodes = deque()
        next_nodes.append((0, 0))

        path_length = 0

        while next_nodes:
            path_length += 1
            for i in range(len(next_nodes)):
                current_row, current_column = next_nodes.popleft()
                if current_row == rows - 1 and current_column == columns - 1:
                    return path_length

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for direction in directions:
                    new_row = current_row + direction[0]
                    new_column = current_column + direction[1]

                    if (new_row in range(rows) and
                        new_column in range(columns) and
                        (new_row, new_column) not in visited and
                        grid[new_row][new_column] == 0):
                        visited.add((new_row, new_column))
                        next_nodes.append((new_row, new_column))

        return -1

'''
1. Start at 0,0, add it to a queue
2. While there are items to visit in the queue
    1. For each element in the queue, pop the element
    2. Check if the element is at the end, if it is at the end return the length
    3. For each possible direction
        1. Check if the direction is within range and it is not visited
        2. Add the element to the queue and to the visited set
    4. Increment the length of path by 1


'''