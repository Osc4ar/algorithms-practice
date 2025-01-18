class Solution:
    '''
    Sliding window, keep track of k
               *         *
    [1,1,1,0,0,0,1,1,1,1,0] 
    k = 0
    max = 6

    Window size = R - L + 1
    '''
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if nums[0] == 1:
                return 1
            if k > 0:
                return 1
        
        left = 0
        max_size = 0
        current_size = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                if zero_count > k:
                    while zero_count > k and left <= right:
                        if nums[left] == 0:
                            zero_count -= 1
                        left += 1

            current_size = right - left + 1
            max_size = max(max_size, current_size)

        return max_size
