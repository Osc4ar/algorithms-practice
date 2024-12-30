class Solution:
    '''
    We can keep a dictionary with the frequency of each letter on s1
    We have a window of the size of s1 to review the characters on s2
    We keep moving the window and verifying against the frequencies of s1 to see
    if s2 has a permutation of s1
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_frequencies = Counter(s1)

        left = 0
        right = len(s1) - 1

        s2_window = s2[left:right+1]
        s2_frequencies = Counter(s2_window)

        while right < len(s2):
            if s2_frequencies == s1_frequencies:
                return True

            s2_frequencies[s2[left]] -= 1
            if right + 1 < len(s2):
                s2_frequencies[s2[right + 1]] += 1

            right += 1
            left += 1 

        return False
