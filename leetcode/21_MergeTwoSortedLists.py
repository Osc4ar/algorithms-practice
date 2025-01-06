# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
              *
    [1, 1, 2, 3, 4]
     *
    [5]
    ''' 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        prev = None
        p1 = list1
        p2 = list2
    
        while p1 or p2:
            if p2 is None:
                return list1

            if p1 is None:
                prev.next = p2
                return list1

            if p1.val <= p2.val:
                prev = p1
                p1 = p1.next
            else:
                if prev:
                    prev.next = p2
                else:
                    list1 = p2
                tmp = p2.next
                p2.next = p1
                prev = p2
                p2 = tmp

        return list1
