class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        total = len(nums)
        target = total / 3

        result = []
        for n, freq in freqs.items():
            if freq > target:
                result.append(n)

        return result
