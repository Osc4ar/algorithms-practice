class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        heap = []
        for num, frequency in frequencies.items():
            heappush(heap, (-1*frequency, num))

        top_k = []
        for _ in range(k):
            frequency, num = heappop(heap)
            top_k.append(num)

        return top_k