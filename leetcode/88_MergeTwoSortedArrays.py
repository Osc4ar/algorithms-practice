class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        merge = m + n - 1

        while i >= 0 or j >= 0:
            if i < 0 and j >= 0:
                nums1[merge] = nums2[j]
                j -= 1
            elif j < 0 and i >= 0:
                nums1[merge] = nums1[i]
                i -= 1
            elif nums1[i] > nums2[j]:
                nums1[merge] = nums1[i]
                i -= 1
            else:
                nums1[merge] = nums2[j]
                j -= 1
            merge -= 1
