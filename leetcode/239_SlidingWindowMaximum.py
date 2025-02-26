class Solution:
    '''
    1. We can keep a sliding window of size k
    2. Create a double-ended queue with the max of the window at the left.
    3. Every time we need to insert a value it should be smaller than the right-most value, if it is not smaller than the right-most value: pop until the value is smaller or the queue is empty
    4. When the index in the left-most position is out of the window, we pop it
    5. For every valid window, save the max value in a result array 
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()
        left = 0

        for right in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)

            if queue[0] < left:
                queue.popleft()

            if right - left == k - 1:
                result.append(nums[queue[0]])
                left += 1

        return result
