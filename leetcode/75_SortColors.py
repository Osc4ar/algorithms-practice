class Solution:
    '''
    We can use a heap sort, which is O(nlogn)
    Another option is build a frequency dictionary, we only expect to have values 0,1 or 2
    Then we modify the nums in place by adding the nums in order. This would be O(n)
    '''
    def sortColors(self, nums: List[int]) -> None:
        freqs = Counter(nums)

        i = 0
        for color in range(3):
            for _ in range(freqs[color]):
                nums[i] = color
                i += 1
        
