class Solution:
    '''
    1. We iterate the grid, if we find a gate which was not visited before
    2. We use BFS on every empty cell we find in the path, we add the distance from the gate
    3. If we find a cell which has a value different than empty or Obstacle, we update it if our count is smaller
    4. We continue searching until we do not have empty cells in the queue
    '''
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        EMPTY = 2**31 - 1
        GATE = 0

        ROWS = range(len(rooms))
        COLS = range(len(rooms[0]))
        queue = deque()

        def bfs(queue):
            distance = 0
            while queue:
                distance += 1
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    directions = [(0,1), (1,0), (0,-1), (-1, 0)]
                    for x, y in directions:
                        new_r = r + x
                        new_c = c + y
                        if (new_r in ROWS and
                            new_c in COLS and
                            rooms[new_r][new_c] == EMPTY):
                            rooms[new_r][new_c] = distance
                            queue.append((new_r, new_c))

        for r in ROWS:
            for c in COLS:
                if rooms[r][c] == GATE:
                    queue.append((r, c))

        bfs(queue)
