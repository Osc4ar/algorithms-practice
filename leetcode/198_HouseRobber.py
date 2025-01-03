class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        best = nums[:]

        for i in reversed(range(len(nums))):
            option1 = 0
            option2 = 0
            if i + 2 < len(nums):
                option1 = best[i+2]
            if i + 3 < len(nums):
                option2 = best[i+3]

            best[i] = nums[i] + max(option1, option2)

        return max(best[0], best[1])
