class Solution:
    '''
    1. Using recursion take the first num in nums, add it to the response
    2. Check if we already have processed that value before, if yes skip the recursive calls
    3. If not, call the recursive function with the rest of nums
    4. We stop if nums is empty or we already processed that num
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        visited = set()
        nums = sorted(nums)

        def backtracking(nums: List[int], current: list):
            if len(nums) == 0:
                return

            current.append(nums[0])
            result.append(current[:])
            current_visited = set()
            for i in range(1, len(nums)):
                if nums[i] not in current_visited:
                    current_visited.add(nums[i])
                    backtracking(nums[i:], current)
            current.pop()

        for i, n in enumerate(nums):
            if n not in visited:
                visited.add(n)
                backtracking(nums[i:], [])

        return result
