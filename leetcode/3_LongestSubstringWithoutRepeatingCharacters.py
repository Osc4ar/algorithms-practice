class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        longest = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in substring:
                longest = max(longest, len(substring))
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1

            substring.add(s[right])

        return max(longest, len(substring))
