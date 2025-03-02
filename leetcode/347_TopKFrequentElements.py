class Solution:
    '''
    1. Get the frequency of every number, save it on a hash map
    2. Save the frequency and number pairs on an array
    3. Heapify that array based on the frequency (max heap)
    4. Pop the k elements

    Time complexity: O(klog(n))
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_num_pairs = [(-1*f, n) for n, f in freq.items()]
        heapq.heapify(freq_num_pairs)

        result = []
        while len(result) < k:
            _, num = heapq.heappop(freq_num_pairs)
            result.append(num)
        
        return result
