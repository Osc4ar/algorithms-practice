# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead = head
        count = 0
        while lead and count < n:
            lead = lead.next
            count += 1

        prev = None
        current = head
        while current:
            if not lead:
                if prev:
                    prev.next = current.next
                    return head
                else:
                    return current.next

            prev = current
            current = current.next
            lead = lead.next
