class Solution:
    '''
    1. Remove all candidates bigger than the target since there is no negative candidates
    2. We can use recursion with backtracking to solve the problem as follows:
        a. Create function which receives the target and a list of candidates
        b. Add the first number to the possible result and call recursively the function with a new target = target - num
        c. Our base case will be when we do not have more candidates or the current_sum is bigger than our target
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        valid = []
        for c in sorted(candidates):
            if c <= target:
                valid.append(c)

        visited = set()
        unique_results = set()
        def backtracking(index: int, target: int, current: List[int]):
            if target == 0:
                t = tuple(current[:])
                if t not in unique_results:
                    results.append(current[:])
                    visited.add(current[0])
                    unique_results.add(t)
                return
            if target < 0:
                return
            if index == len(valid):
                return

            num = valid[index]
            if num not in visited:
                current.append(num)
                backtracking(index + 1, target - num, current)
                current.pop()

            backtracking(index + 1, target, current)

        if len(valid) == 0:
            return []

        backtracking(0, target, [])
        return results
