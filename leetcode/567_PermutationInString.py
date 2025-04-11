class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs_s1 = Counter(s1)
        freqs_s2 = Counter(s2[:len(s1)])

        if freqs_s1 == freqs_s2:
            return True

        left = 0
        right = len(s1)
        for right in range(len(s1), len(s2)):
            freqs_s2[s2[right]] += 1
            freqs_s2[s2[left]] -= 1

            if freqs_s1 == freqs_s2:
                return True

            left += 1

        return False
