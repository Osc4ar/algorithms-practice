# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = l1.val + l2.val

        base10 = s % 10
        remaining = s // 10

        result = ListNode(val=base10)

        current_l1 = l1.next
        current_l2 = l2.next
        current_result = result
        while current_l1 or current_l2 or remaining > 0:
            current_sum = remaining

            if current_l1:
                current_sum += current_l1.val
                current_l1 = current_l1.next
            if current_l2:
                current_sum += current_l2.val
                current_l2 = current_l2.next

            base10 = current_sum % 10
            remaining = current_sum // 10
            current_result.next = ListNode(val=base10)
            current_result = current_result.next

        return result
