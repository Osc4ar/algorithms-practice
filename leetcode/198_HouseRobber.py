class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}
        def recursive(index: int) -> int:
            if index >= len(nums):
                return 0

            if index in memory:
                return memory[index]
    
            first = nums[index] + recursive(index + 2)
            if index + 1 < len(nums):
                second = nums[index + 1] + recursive(index + 3)
            else:
                second = 0

            memory[index] = max(first, second)

            return memory[index]

        return recursive(0)
