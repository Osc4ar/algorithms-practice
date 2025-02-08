class Solution:
    '''
    Since we do not need to modify the string, we only need to count how many parentheses are unbalanced

    1. We could use a counter variable starting at zero
    2. For every opening parenthesis we increase count by one
    3. For every closing parenthesis we decrease count by one
    4. If the count is already zero, we add the closing parenthesis to another count of extra closing parenthesis
    4. We return the sum of count plus any extra closing parenthesis as result
    '''
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        extra_closing = 0

        for c in s:
            if c == '(':
                count += 1
            elif count > 0:
                count -= 1
            else:
                extra_closing += 1

        return count + extra_closing
