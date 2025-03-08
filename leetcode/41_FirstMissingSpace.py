class Solution:
    '''
    1. Instead of using a set, we can use the array as a set to know if a given number exists
    2. The solution will be on the range [1, len(nums)+1]
    3. Iterate the array and change all negative numbers to be 0
    4. Iterate once again the array and then mark with a negative sign if the num exists on the array
    5. To do this, first check if the index of the num: num - 1 is on the array bounds, if it is not that means we can ignore it since it is outside our solution's range
    6. Iterate once again, in this case the range of the solutions and return the first number which is positive in our array
    7. If we finish the iteration without finding a positive number, then we return len(nums) + 1
    8. If the value in the index of the position nums - 1 is zero, use -1*(len(nums)+1) as the value since it is out of range
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            target = abs(nums[i]) - 1

            if target >= 0 and target < len(nums):
                if nums[target] > 0:
                    nums[target] *= -1
                elif nums[target] == 0:
                    nums[target] = -1*(len(nums) + 1)

        for n in range(1, len(nums) + 1):
            target = n - 1
            if nums[target] >= 0:
                return n

        return len(nums) + 1
