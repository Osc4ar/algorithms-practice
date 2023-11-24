class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        max_len = 0
        
        for i in range(len(s)):
            # odd palindromes like aba
            left, right = i, i
            odd_result = self.currentCenterLongestPalindrome(s, left, right)
            if len(odd_result) > max_len:
                result = odd_result
                max_len = len(odd_result)
            
            # even palindromes like bb
            left, right = i, i+1
            even_result = self.currentCenterLongestPalindrome(s, left, right)
            if len(even_result) > max_len:
                result = even_result
                max_len = len(even_result)
                
        return result
        
    def currentCenterLongestPalindrome(self, s: str, left: int, right: int) -> str:
        result = ''
        max_len = 0
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_palindrome = s[left:right+1]
            current_len = len(current_palindrome)

            if current_len > max_len:
                result = current_palindrome
                max_len = current_len
                
            left -= 1
            right += 1
                
        return result
'''
abb
result = a
max_len = 1

a
odd
l=0, r=0
even
fails

b
odd
l=1, r=1
l=0, r=2

even
l=1, r=2
result = bb
max_len = 1
'''