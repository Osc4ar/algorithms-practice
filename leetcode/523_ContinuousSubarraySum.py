class Solution:
    '''
    [23, 25, 29, 35, 42]
    [5, 1, 5, 5, 0]

    arr = {
        0: -1
    }
    '''
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        remainders = {
            0: -1
        }
        prefix = 0
        for i, n in enumerate(nums):
            prefix += n
            current = prefix % k
            if current in remainders:
                prev_index = remainders[current]
                if i - prev_index >= 2:
                    return True
            else:
                remainders[current] = i

        return False
