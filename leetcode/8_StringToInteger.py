class Solution:
    def myAtoi(self, s: str) -> int:
        digits = '0123456789'
        lower_limit = (-1) * 2**31
        upper_limit = 2**31 - 1

        numbers = []
        negative = False
        sign_read = False
        for c in s:
            if c not in digits and (len(numbers) or sign_read):
                break

            if c in digits:
                numbers.append(int(c))
            elif c == '-':
                negative = True
                sign_read = True
            elif c == '+':
                sign_read = True
            elif c == ' ':
                continue
            else:
                break

        result = 0
        for i, n in enumerate(reversed(numbers)):
            result += n * 10**i

        if negative:
            result *= -1

        if result > upper_limit:
            return upper_limit
        if result < lower_limit:
            return lower_limit

        return result
