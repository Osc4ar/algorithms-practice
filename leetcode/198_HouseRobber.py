class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        option1 = nums[0] + self.rob(nums[2:])
        option2 = nums[1] + self.rob(nums[3:])
        return max(option1, option2)
        

'''
[1,10,30,10,1]
max(1 + rob(30, 10, 1), 10 + rob(10, 1)) -> max(1 + 31, 10 + 10) -> max(32, 20) -> 32

[30, 10, 1]
max(30 + rob(1), 10 + rob()) -> max(30 + 1, 10) -> max(31, 10) -> 31

[10, 1]
max(rob(10), rob(1)) -> max(10, 1) -> 10
'''