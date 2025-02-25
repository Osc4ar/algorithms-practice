class Solution:
    '''
    1. Create a sliding window of size k in the left
    2. Keep a count of each value on the window and the max value using a max heap of the unique values
    3. Every time we move a position to the right, remove the leftmost element from the count
    4. If it is zero, remove it from the count and the max heap, keep removing values until we have one that exists on the count
    5. Add the new value to the heap and the count
    6. Save the max of every window
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = defaultdict(int)
        max_heap = []

        for right in range(k):
            n = nums[right]
            if n not in count:
                heapq.heappush(max_heap, -1*n)
            count[n] += 1
        result.append(-1*max_heap[0])

        left = 0
        for right in range(k, len(nums)):
            old = nums[left]
            if count[old] == 1:
                count.pop(old)
                while max_heap and -1*max_heap[0] not in count:
                    heapq.heappop(max_heap)
            else:
                count[old] -= 1
            left += 1

            new = nums[right]
            count[new] += 1
            heapq.heappush(max_heap, -1*new)
            result.append(-1*max_heap[0])

        return result
