class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                return self.binary_search(nums, target, left, right)
            
            middle = (right + left) // 2
            if target == nums[middle]:
                return middle
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right

            if target > nums[middle] and (target < nums[right] or nums[middle] > nums[right]):
                left = middle + 1
            elif target < nums[left] and nums[left] < nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            middle = (right + left) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        
        return -1
