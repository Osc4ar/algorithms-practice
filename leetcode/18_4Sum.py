class Solution:
    '''
    [-2, -1, 0, 0, 1, 2]

    1. Sort the array
    2. Taken one element to create a new temp target
    3. Execute three sum on the rest of the array with the new target
    4. Repeat for every number, if we already calculated 3sum for that target skip

    3Sum:
    1. Take the first value and create a temp target.
    2. Create a left and right pointer, one at the start and the other at the end of the array
    3. If the sum of the three values is less than the target, move the left pointer to the right.
    4. If the sum of the tree values is bigger than the target, move the right pointer to the left
    5. Repeat this for every element on the array
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        visited = set()
        result = []

        def threeSum(nums: List[int], target: int, first_num: int):
            visited = set()
            for i, n in enumerate(nums):
                if n in visited:
                    continue

                visited.add(n)
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    current = n + nums[left] + nums[right]
                    if current < target:
                        left += 1
                    elif current > target:
                        right -= 1
                    else:
                        result.append([first_num, n, nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1

        for i, n in enumerate(sorted_nums):
            if n not in visited:
                threeSum(sorted_nums[i+1:], target - n, n)
                visited.add(n)

        return result
