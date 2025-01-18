# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = None
        prev = None
        p1 = l1
        p2 = l2
        while p1 or p2 or carry:
            new_val = carry
            if p1 is not None:
                new_val += p1.val
                p1 = p1.next
            if p2 is not None:
                new_val += p2.val
                p2 = p2.next

            carry = new_val // 10
            new_val = new_val % 10

            if prev is None:
                result = ListNode(val=new_val)
                prev = result
            else:
                prev.next = ListNode(val=new_val)
                prev = prev.next

        return result
