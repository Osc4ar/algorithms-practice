class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        second_to_last = 1
        last = 2
        result = 0
        for i in range(2, n):
            result = last + second_to_last
            second_to_last = last
            last = result

        return result
