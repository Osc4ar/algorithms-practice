class Solution:
    '''
    1. Sort the array to make the search faster with two pointers [-4, -1, -1 0, 1, 2]
    2. Take the first value x and focus in solve two sum
    3. Since the array is sorted we can have two pointers, one in the beginning of the search
    and another at the end.
    4. If the number is smaller than the target, we move the left pointer
    5. If the number is greater than the target, we move the right pointer
    6. If we find the target we save the result and keep looking moving the left pointer

          x     *  *
    [-4, -1, -1 0, 1, 2]
    target = 1
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)

        result = []
        visited = set()
        # O(n^2)
        for i, n in enumerate(nums):
            if n in visited:
                continue

            target = -1*n
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[left] + nums[right]
                if current == target:
                    result.append([nums[i], nums[left], nums[right]])
                    prev = nums[left]
                    while left < len(nums) and prev == nums[left]:
                        left += 1
                elif current < target:
                    left += 1
                else:
                    right -= 1

            visited.add(n)

        return result
