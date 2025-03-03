class Solution:
    '''
    We can save the number of jumps needed to reach an element nums[i] on an array,
    we will always keep the minimum number of jumps in the position i
       *
    [2,3,1,1,4]
    [1,1,1,2,2]

    1. Initialize the array with a size n full of infinites
    2. While the last cell is equal to infite do the following:
        1. For every next number between [i+1,i+j]
        2. Check the sum to reach that next value by visiting the current cell: jumps[i]+1
        3. Save in that cell the min between that value and the current value saved: min(jums[i]+1, jumps[i+j])
    3. After finishing this, the result will be on the last cell
    '''
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        i = 0
        while dp[-1] == float('inf') and i < len(nums):
            for j in range(1, nums[i]+1):
                if i+j == len(nums):
                    break

                current = dp[i] + 1
                dp[i+j] = min(dp[i+j], current)
            i += 1

        return dp[-1]
