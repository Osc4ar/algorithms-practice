class Solution:
    def reverseBits(self, n: int) -> int:
        result = n & 1

        for _ in range(31):
            result = result << 1
            n = n >> 1

            result += n & 1

        return result