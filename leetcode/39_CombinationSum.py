class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        response = self.findSum([], candidates, target, result)

        return result

    def findSum(self, sum_path: List[int], candidates: List[int], target: int, result: List[List[int]]) -> bool:
        if target == 0:
            return True
        if target < 0:
            return False

        for i, candidate in enumerate(candidates):
            if candidate <= target: # 7
                sum_path.append(candidate) # [2]
                new_target = target - candidate # 5

                isValidSum = self.findSum(sum_path, candidates[i:], new_target, result)
                if isValidSum:
                    result.append(sum_path.copy())

                sum_path.pop()

        return False

'''
candidates = [2, 3, 6, 7], target = 7

1. Append the ith candidate to the sum path
2. Check if the ith candidate + the other candidates are True
3. Pop the ith candidate if not
4. Repeat that for each candidate
'''