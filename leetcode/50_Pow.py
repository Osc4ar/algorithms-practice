class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive(x: float, n: int) -> float:
            if n == 0 or x == 1:
                return 1

            res = recursive(x * x, n // 2)
            if n % 2 == 1:
                res *= x

            return res

        result = recursive(x, abs(n))

        if n < 0:
            return 1 / result
        return result

