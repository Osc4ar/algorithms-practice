class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]

        while left <= right:
            if left > 0 and nums[left - 1] > nums[left]:
                return nums[left]
            if right < len(nums) - 1 and nums[right + 1] < nums[right]:
                print('this case')
                return nums[right + 1]
            if nums[left] < nums[right]:
                return nums[left]

            left += 1
            right -= 1

        return nums[left]