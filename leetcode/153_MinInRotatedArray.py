class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        result = nums[left]

        while left <= right:
            if nums[left] < nums[right]:
                return min(result, nums[left])

            middle = (right + left) // 2
            result = min(result, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return result