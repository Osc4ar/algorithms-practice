"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        cloned_first_node = Node(val=node.val)
        cloned_nodes = {
            1: cloned_first_node
        }

        next_nodes = deque()
        next_nodes.append(node)

        while next_nodes:
            for _ in range(len(next_nodes)):
                original_node = next_nodes.popleft()
                cloned_node = cloned_nodes[original_node.val]

                for neighbor in original_node.neighbors:
                    if neighbor.val not in cloned_nodes:
                        cloned_nodes[neighbor.val] = Node(val=neighbor.val)
                        next_nodes.append(neighbor)

                    cloned_neighbor = cloned_nodes[neighbor.val]
                    cloned_node.neighbors.append(cloned_neighbor)

        return cloned_first_node
