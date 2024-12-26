class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        left = 0
        right = 0
        max_size = 1
        frequencies = {s[right]: 1}

        while right < len(s):
            size = right - left + 1
            max_frequency = self.getMaxFrequency(frequencies)
            if size - max_frequency <= k:
                max_size = max(max_size, size)
                right += 1
                if right < len(s):
                    self.increaseFrequency(frequencies, s[right])
            else:
                frequencies[s[left]] -= 1
                left += 1

        return max_size

    def increaseFrequency(self, frequencies: dict[str, int], key: str):
        if key not in frequencies:
            frequencies[key] = 1
        else:
            frequencies[key] += 1

    def getMaxFrequency(self, frequencies: dict[str, int]) -> int:
        max_f = 0
        for key, frequency in frequencies.items():
            max_f = max(max_f, frequency)
        return max_f
