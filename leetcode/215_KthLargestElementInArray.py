class Solution:
    '''
    Min heap of size k with the biggest values:
               * 
    [3,2,1,5,6,4]

                   4
                6     5
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            elif n > heap[0]:
                heapq.heappushpop(heap, n)

        return heap[0]
