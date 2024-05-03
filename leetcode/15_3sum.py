class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = n + nums[left] + nums[right]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]])
                    old_value = nums[left]
                    while left < len(nums) and old_value == nums[left]:
                        left += 1

        return result
