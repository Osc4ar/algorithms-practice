class Solution:
    '''
    prefix = 1
    suffix = 1
    [1, 2, 3, 4]
        *
    [1, 1, 1, 1]
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] * nums[i]

        suffix[-1] = nums[-1]
        for i in reversed(range(0, len(prefix) - 1)):
            suffix[i] = suffix[i+1] * nums[i]

        result[0] = suffix[1]
        result[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            result[i] = prefix[i-1] * suffix[i+1]
        return result
