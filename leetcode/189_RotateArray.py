class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        1. Mark the last k elements with a placeholder to be removed
        2. Save the last k elements in a separate array
        3. Move the remaining elements from their original position to fill the placeholders
        4. Copy the last k elements to the beginning of the array
        5. We can reduce k to be the module of the array size, we do not need to shift multiple times
        """
        real_k = k % len(nums)

        if real_k == 0:
            return

        # Save the last k elements
        queue = deque()
        for i in range(len(nums)-real_k, len(nums)):
            queue.append(nums[i])
        
        # Shift the elements in the array to the end
        left = len(nums) - 1 - real_k
        right = len(nums) - 1
        while left >= 0:
            nums[right] = nums[left]
            left -= 1
            right -= 1

        # Copy saved elements to beginning of array
        i = 0
        while queue:
            nums[i] = queue.popleft()
            i += 1 
