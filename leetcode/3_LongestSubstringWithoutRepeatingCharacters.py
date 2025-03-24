class Solution:
    '''
    1. Use sliding window technique, both pointers will start at 0
    2. Keep a set to know if there is duplicates
    3. Expand right pointer one position, if the string is on the set reduce the window until the window is valid again
    4. Once we have a valid window, we save the max window size as the result
    5. After iterating the whole array return the max window size
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        chars = set()
        left = 0
        for right in range(len(s)):
            while left < right and s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])
            result = max(result, len(chars))

        return result
