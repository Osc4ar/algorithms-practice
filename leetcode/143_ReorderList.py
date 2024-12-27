# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the second half of the list
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        current = slow.next
        slow.next = None
        new_next = None
        while current:
            tmp = current.next
            current.next = new_next
            new_next = current
            current = tmp
        
        # merge the lists
        current1 = head
        current2 = new_next
        while current2:
            tmp1 = current1.next
            tmp2 = current2.next

            current1.next = current2
            current2.next = tmp1

            current2 = tmp2
            current1 = tmp1
