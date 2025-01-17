class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = s.lower()
        cleaned = re.sub('[^a-z0-9]', '', lower_case)

        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
