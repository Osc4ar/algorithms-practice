class Solution:
    '''
    Generate the permutation using Backtracking as follows:
    1. Iterate nums, we have the option to either take the number or skip it
    2. If we take it, we have to call the recursive function with all nums except the one we took
    3. To avoid duplicates, before saving the permutation we check if it is already on the results, if not we add it
    4. To avoid repeated work, if we already added a number to the current permutation, we do not need to repeat that permutation group
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtracking(nums: List[int], current: List[int]):
            if len(nums) == 0:
                t = tuple(current)
                if t not in result:
                    result.add(t)
                return

            visited = set()
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    new_nums = nums[:i] + nums[i+1:]
                    current.append(nums[i])
                    backtracking(new_nums, current)
                    current.pop()

        backtracking(nums, [])

        return [list(perm) for perm in result]
