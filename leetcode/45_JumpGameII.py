class Solution:
    '''
    Instead of using a queue, we can keep the range we are visiting with a left and right pointers
    1. The value we can visit at the beginning is zero
    2. For every value in our window, we check the farthest we can reach
    3. The new window will be from the value next to the original window to the farthest element we can reach
    4. As soon as the window reaches the last element in our array, we finish the iteration
    '''
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            max_jump = 0
            for i in range(left, right+1):
                max_jump = max(max_jump, i + nums[i])
            left = right + 1
            right = max_jump
            jumps += 1

        return jumps
