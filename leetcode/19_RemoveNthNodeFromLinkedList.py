# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        if size == 1:
            return None

        target = size - n + 1

        i = 0
        prev = None
        current = head
        while i < target:
            i += 1
            if i == target:
                if prev:
                    prev.next = current.next
                else:
                    return current.next
            
            prev = current
            current = current.next

        return head