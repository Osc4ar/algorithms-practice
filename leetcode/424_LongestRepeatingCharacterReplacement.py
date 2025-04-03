class Solution:
    '''
      L  R
    AABABBA

    1. Store the frequency of each letter on a HashMap
    2. Any time we expand our window, add one to the letter
    3. Find the most common letter, check if its Window Size - Frequency is less than or equal than k
    4. If it is, we have a valid window, save it if it is bigger than the previous one
    5. If it is not, reduce the window size.
    6. While reducing the window size, check if the most common letter changes.
    7. Reduce the window until it is valid again
    8. Return the max window calculated after iterating the whole array
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        freqs = defaultdict(int)

        for right in range(len(s)):
            freqs[s[right]] += 1
            window_size = right - left + 1
            most_frequent = max(freqs.values()) # O(26)

            while left <= right and window_size - most_frequent > k:
                freqs[s[left]] -= 1
                left += 1
                most_frequent = max(freqs.values()) # O(26)
                window_size = right - left + 1

            result = max(result, window_size)

        return result
