class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        intersect = False
        while not intersect:
            slow = nums[slow]
            fast = nums[nums[fast]]
            intersect = slow == fast
        
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

        return slow
