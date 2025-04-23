class Solution:
    '''
    Use sliding window technique as follows:
    1. If the character is on t, start increasing the window
    2. Save the frequency of each letter in a Counter, if the counters are the same save the window size
    3. If we reach the end of the string and the Counter did not match, stop the search
    4. We can reduce the left side if the frequency of that letter is bigger in our window than in the target Counter
    '''
    def minWindow(self, s: str, t: str) -> str:
        min_size = len(s)+1
        result = (0, 0) # We will save the left and right positions to do s[left:right]

        s_freqs = defaultdict(int)
        t_freqs = Counter(t)
        left = 0
        while left < len(s):
            if s[left] in t_freqs:
                s_freqs[s[left]] += 1

                if self.is_valid_window(s_freqs, t_freqs):
                    return s[left:left+1]

                right = left + 1
                left_adjusted = False
                while right < len(s):
                    c = s[right]
                    s_freqs[c] += 1

                    while s[left] not in t_freqs or s_freqs[s[left]] > t_freqs[s[left]]:
                        s_freqs[s[left]] -= 1
                        left += 1
                        left_adjusted = True

                    if self.is_valid_window(s_freqs, t_freqs):
                        size = right - left + 1
                        if size < min_size:
                            result = (left, right+1)
                            min_size = size

                    right += 1
                s_freqs = defaultdict(int)
                if not left_adjusted:
                    left = right + 1
            else:
                left += 1

        if result == (0,0):
            return ""
        return s[result[0]:result[1]]

    def is_valid_window(self, current: dict, target: Counter) -> bool:
        for k in target.keys():
            if current[k] < target[k]:
                return False
        return True
