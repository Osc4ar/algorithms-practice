# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1. We can merge all the lists on the first one, we will have two main scenarios:
        1. If the smallest node is on the first list, we move its pointer one position
        2. If the smallest node is on any other list we will:
            1. Point the previous node of the first list to this new smallest node
            2. Move the list with the smallest node to its next node
            3. Make the smallest node point to the current item on the first list
            4. Make the smallest node the new previous node
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        pointers = lists[:]
        prev = None
        non_empty = 1
        head = None
        while non_empty > 0:
            smallest_index = 0
            smallest_val = float('inf')
            non_empty = 0
            to_remove = []
            for i, p in enumerate(pointers):
                if p is None:
                    to_remove.append(i)
                    continue
                
                non_empty += 1
                if p.val < smallest_val:
                    smallest_val = p.val
                    smallest_index = i

            if non_empty == 0:
                break

            if smallest_index == 0:
                prev = pointers[0]
                pointers[0] = pointers[0].next
            else:
                if prev is None:
                    tmp = pointers[smallest_index].next
                    pointers[smallest_index].next = pointers[0]
                    prev = pointers[smallest_index]
                    pointers[smallest_index] = tmp
                else:
                    prev.next = pointers[smallest_index]
                    pointers[smallest_index] = pointers[smallest_index].next
                    prev.next.next = pointers[0]
                    prev = prev.next

            if head is None:
                head = prev

            for i in reversed(to_remove):
                if i != 0:
                    pointers.pop(i)

        return head
