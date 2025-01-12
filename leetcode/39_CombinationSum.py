class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtracking(index: int, current: List[int], total: int):
            if total == target:
                results.append(current.copy())
                return
            if index == len(candidates) or total > target:
                return

            candidate = candidates[index]
            current.append(candidate)
            backtracking(index, current, total + candidate)
            current.pop()

            backtracking(index + 1, current, total)

        backtracking(0, [], 0)
        return results
