class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for index, num in enumerate(nums):
            if num in complements:
                previous_index = complements[num]
                return [previous_index, index]
            
            complements[target - num] = index
        
        return [-1, -1]