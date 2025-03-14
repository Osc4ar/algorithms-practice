class Solution:
    '''
    1. Find the first duplicate from right to left, that will be the last element to remove
    2. The index of that element, divided by 3 is the number of removals we have to do to have a distinct array
    3. We have to round up the division because we have to remove the duplicate completely
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        freqs = defaultdict(int)

        index = 0
        for i in reversed(range(len(nums))):
            if freqs[nums[i]] == 1:
                index = i + 1
                break
            freqs[nums[i]] += 1

        return math.ceil(index / 3)
