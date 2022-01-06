class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivotIndex = int(len(nums) / 2)
        pivot = nums[pivotIndex]
    
        left_nums = nums[:pivotIndex]
        right_nums = nums[pivotIndex:]
    
        if pivot == target:
            return pivotIndex
        if len(nums) == 1: 
            return -1
        
        if pivot > target:
            return self.search(left_nums, target)
        if pivot < target:
            result = self.search(right_nums, target)
            
            if result != -1:
                result += pivotIndex

            return result
