# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                node = lists[i]
                heapq.heappush(heap, (node.val, i, node))

        head = ListNode()
        current = head
        while heap:
            _, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next
