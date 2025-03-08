class Solution:
    '''
    1. Convert the array to a set for fast checks
    2. Start a range from 1 to max(array)+1, check if the integer is on the set
    3. If it is not in the set, return the num
    4. If it is in the set, we will iterate n+1 times
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        a_set = set(nums)
        upper_limit = max(a_set)
        
        if upper_limit < 0:
            return 1

        for n in range(1, (upper_limit + 1) + 1):
            if n not in a_set:
                return n
        
        return upper_limit + 1
