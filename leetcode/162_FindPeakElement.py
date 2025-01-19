class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        index = (len(nums) - 1) // 2
        while index in range(len(nums)):
            right = True
            if index+1 < len(nums) and nums[index+1] > nums[index]:
                right = False
            left = True
            if index-1 >= 0 and nums[index-1] > nums[index]:
                left = False

            if left and right:
                return index

            if left and not right:
                index += 1
            else:
                index -= 1

        return -1
