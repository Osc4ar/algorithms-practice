"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
    1. Create a duplicate of each Node between the node and its next Node
    2. The duplicates will only have the value and next pointer, but no random pointer
    3. Now we will iterate every original node, if we have a random pointer then we will do something like:
        node.next.random = node.random.next
       This will set the random pointer of the copy Node to be the next node after the random node, which is the copy we made
    4. We separate the copied nodes to a separated list and restore the original list
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        current = head
        while current:
            copy = Node(current.val)

            if current.next:
                copy.next = current.next

            current.next = copy
            current = copy.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        copy_head = head.next
        current = head
        while current:
            copy = current.next
            current.next = copy.next
            if current.next:
                copy.next = current.next.next
            else:
                copy.next = None

            current = current.next

        return copy_head
