class Solution:
    '''
    Use a sliding window technique, starting at zero position both pointers

    1. Keep moving the right pointer to the right one by one
    2. For the left, we have to check if the sum is positive
    3. If it is not move the pointer to the right until the sum is positive or we reach the right pointer
    4. We save the max sum in a variable, return the max sum once we finish the iteration


                LR
    [-2, 1, -3, 4]

    [5, 4, -1, 7, 8]
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        current = 0
        result = float('-inf')
        for right, n in enumerate(nums):
            current += n

            while (current <= 0 or nums[left] < 0) and left < right:
                current -= nums[left]
                left += 1

            result = max(result, current)

        return result
