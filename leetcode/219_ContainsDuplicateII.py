class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                values.remove(nums[left])
                left += 1
            if nums[right] in values:
                return True
            values.add(nums[right])

        return False
