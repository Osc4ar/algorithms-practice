class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = set()

        def recursion(nums: List[int], perm: List[int], results: set):
            if len(nums) == 0:
                t = tuple(perm)
                if t not in results:
                    results.add(t)
                return
            
            visited = set()
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    new_nums = nums[:i] + nums[i+1:]
                    perm.append(nums[i])
                    recursion(new_nums, perm, results)
                    perm.pop()

        recursion(nums, [], results)

        return [list(perm) for perm in results]
