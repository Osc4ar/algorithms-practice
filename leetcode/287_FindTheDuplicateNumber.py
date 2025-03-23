class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                result = abs(nums[i])
                break
            
            nums[abs(nums[i]) - 1] *= -1

        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return result
