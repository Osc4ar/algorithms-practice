class Solution:
    def rob(self, nums: List[int]) -> int:
        nonAdjancentMax = 0
        adjancentMax = 0

        for n in nums:
            temp = adjancentMax
            adjancentMax = max(nonAdjancentMax + n, adjancentMax)
            nonAdjancentMax = temp

        return adjancentMax

'''
[2, 4, 8, 9, 9, 3]
[2, ], max(rob1+2, rob2) rob1 = 0, rob2 = 0
[2, 4, ], max(rob1+4, rob2) rob1 = 0, rob2 = 2
[2, 4, 8, ], max(rob1+8, rob2) rob1 = 2, rob2 = 4
[2, 4, 8, 13, ], max(rob1+9, rob2) rob1 = 4, rob2 = 10
[2, 4, 8, 13, 19, ], max(rob1+9, rob2) rob1 = 10, rob2 = 13
[2, 4, 8, 13, 19, 19], max(rob1+3, rob2) rob1 = 13, rob2 = 19
'''