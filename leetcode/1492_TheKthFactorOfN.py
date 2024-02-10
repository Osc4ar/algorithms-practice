class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors_count = 0
        factor = -1

        for i in range(1, n + 1):
            if n % i == 0:
                factors_count += 1
                factor = I

            if factors_count == k:
                return factor


        return -1
