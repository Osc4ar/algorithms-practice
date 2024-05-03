'''
1. We sort the numbers
2. We iterate the every element
3. For each element, we create a Left and a Right pointer
4. We move the pointers based on the sum of the three elements while Left < Right
4a. If the result is less than zero we increase the left pointer
4b. If the result is greater than zero we reduce the right pointer
4c. If the result is equal to zero we add the triplet to the result - Note: We continue the iteration since there can be multiple results
5. If the next value is the same than the previous one, we continue to the next one to avoid duplicates
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        result = []
        for i, n in enumerate(sorted_nums):
            if i > 0 and n == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = n + sorted_nums[left] + sorted_nums[right]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    result.append([n, sorted_nums[left], sorted_nums[right]])
                    old_value = sorted_nums[left]
                    while left < len(nums) and old_value == sorted_nums[left]:
                        left += 1

        return result
