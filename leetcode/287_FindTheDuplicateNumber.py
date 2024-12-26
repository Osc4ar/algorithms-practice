class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a_set = set()

        for n in nums:
            if n in a_set:
                return n
            a_set.add(n)
