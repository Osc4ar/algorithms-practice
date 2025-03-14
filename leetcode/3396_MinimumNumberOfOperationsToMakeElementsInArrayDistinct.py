class Solution:
    '''
    1. Count the frequencies of each number on the array
    2. If all frequencies are one, return 0
    3. Initialize a count in zero
    4. Iterate the first three nums, remove them from the count and check if all frequencies are one or zero
    5. Repeate until the array is empty or all frequencies are equal or less than one
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        freqs = Counter(nums)

        count = 0
        index = 0
        while not self.distinct(freqs):
            for i in range(index, min(index+3, len(nums))):
                freqs[nums[i]] -= 1
            index += 3
            count += 1

        return count


    def distinct(self, freqs) -> bool:
        for val, count in freqs.items():
            if count > 1:
                return False
        return True
