class Solution:
    '''
    c(n) = c(n-1) + c(n-2)
    '''
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 2
        before_prev = 1
        for i in range(2, n):
            tmp = prev
            prev += before_prev
            before_prev = tmp

        return prev
