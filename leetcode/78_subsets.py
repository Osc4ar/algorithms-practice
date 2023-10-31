class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.dfs(0, nums, [], result)

        return result


        
    def dfs(self, index: int, nums: List[int], subset: List[int], result: List[List[int]]):
        if index >= len(nums):
            result.append(subset.copy())
            return

        self.dfs(index + 1, nums, subset, result)

        subset.append(nums[index])
        self.dfs(index + 1, nums, subset, result)
        subset.pop()

