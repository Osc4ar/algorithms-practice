class Solution:
    def longestPalindrome(self, s: str) -> str:
        possible_palindromes = deque()
        possible_palindromes.append(s)
        
        visited = set()
        visited.add(s)

        while possible_palindromes:
            for _ in range(len(possible_palindromes)):
                current_s = possible_palindromes.popleft()

                if self.isPalindrome(current_s):
                    return current_s

                option1 = current_s[:-1]
                if option1 not in visited:
                    visited.add(option1)
                    possible_palindromes.append(option1)

                option2 = current_s[1:]
                if option2 not in visited:
                    visited.add(option2)
                    possible_palindromes.append(option2)

        return s[0]


    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True