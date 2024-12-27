class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        result = 1
        frequencies = {}
        left = 0
        for right in range(len(s)):
            if s[right] not in frequencies:
                frequencies[s[right]] = 1
            else:
                frequencies[s[right]] += 1

            max_frequency = self.getMaxFrequency(frequencies)
            window_size = right - left + 1
            is_valid_str = window_size - max_frequency <= k

            if is_valid_str:
                result = max(result, window_size)
            else:
                while not is_valid_str:
                    frequencies[s[left]] -= 1
                    left += 1
                    window_size = right - left + 1
                    is_valid_str = window_size - max_frequency <= k
            
        return result

    def getMaxFrequency(self, frequencies: [str, int]) -> int:
        max_frequency = 0

        for frequency in frequencies.values():
            max_frequency = max(max_frequency, frequency)

        return max_frequency