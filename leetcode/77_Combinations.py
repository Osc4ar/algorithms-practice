class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def backtracking(current: list[int], limit: int, size: int):
            if len(current) == size:
                results.append(current[:])
                return

            last_value = current[-1]
            for i in range(last_value + 1, limit + 1):
                current.append(i)
                backtracking(current, limit, size)
                current.pop()

        for i in range(1, n+1):
            backtracking([i], n, k)

        return results
