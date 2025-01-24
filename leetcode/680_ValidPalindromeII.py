class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:
            are_different = s[left] != s[right]
            if are_different:
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

            right -= 1
            left += 1

        return True
