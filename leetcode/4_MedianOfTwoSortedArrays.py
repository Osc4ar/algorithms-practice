class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = len(nums1) + len(nums2)
        target = size // 2
        is_even = size % 2 == 0

        median = 0
        prev = 0
        count = -1
        i = 0
        j = 0
        while count < target:
            prev = median
            if j == len(nums2):
                median = nums1[i]
                i += 1
            elif i == len(nums1):
                median = nums2[j]
                j += 1
            elif nums1[i] < nums2[j]:
                median = nums1[i]
                i += 1
            else:
                median = nums2[j]
                j += 1
            count += 1

        if is_even:
            return (median + prev) / 2
        return median
