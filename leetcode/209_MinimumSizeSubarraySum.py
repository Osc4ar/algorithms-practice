class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = len(nums) + 1
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_size = min(min_size, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if min_size > len(nums):
            return 0
        return min_size
