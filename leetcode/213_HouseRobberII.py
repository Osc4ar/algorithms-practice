class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        return max(self.robI(nums[1:]), self.robI(nums[:-1]))

    def robI(self, nums: List[int]) -> int:
        nonAdjacent = 0
        adjacent = 0

        for n in nums:
            tmp = adjacent
            adjacent = max(adjacent, nonAdjacent + n)
            nonAdjacent = tmp

        return adjacent
