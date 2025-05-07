class Solution:
    '''
    1. Create an adjacency list with the array edges
    2. Iterate all nodes from 0 to n,
    3. Using BFS, visit all the nodes we can reach starting on a given node, keep track of the visited nodes to avoid duplicates
    4. If we finish the BFS of the current node, increment the count of components
    5. We only do BFS on the not visited nodes
    '''
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        components = 0
        visited = set()

        def bfs(start: int):
            queue = deque()
            queue.append(start)

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    visited.add(node)
                    for next_node in adj[node]:
                        if next_node not in visited:
                            visited.add(next_node)
                            queue.append(next_node)

        for i in range(n):
            if i not in visited:
                components += 1
                bfs(i)

        return components
