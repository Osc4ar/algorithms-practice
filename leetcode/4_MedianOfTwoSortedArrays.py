class Solution:
    '''
    If we merge the array it would be O(n+m) complexity
    Then we only need to measure the median of the merged array

    The complexity of doing the binary search with both arrays separated is that
    the elements inside the array can be mixed, finding the median of each array will not
    give us the median of the two directly

    What we know is that the median will be (nums1 + nums2) // 2, therefore it will have (nums1+nums2)//2-1 elements on the left of it. We can use the fact that the two arrays are sorted and keep moving them until we find the value at the (nums1+num2)//2 position.

    We can have two pointer for doing this, check which one has the smaller value and move it, until we find the median element.

    If the merged array would be even, we will need to get the average between (nums1+nums2)//2 and its previous value
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) > 0 and len(nums2) == 0:
            mid = len(nums1) // 2
            is_even = len(nums1) % 2 == 0

            if not is_even:
                return nums1[mid]
            
            return (nums1[mid] + nums1[mid-1]) / 2
        if len(nums2) > 0 and len(nums1) == 0:
            mid = len(nums2) // 2
            is_even = len(nums2) % 2 == 0

            if not is_even:
                return nums2[mid]
            
            return (nums2[mid] + nums2[mid-1]) / 2

        merged_size = len(nums1) + len(nums2)
        target = merged_size // 2
        is_even = merged_size % 2 == 0

        prev = 0
        value = 0
        count = -1
        i = 0
        j = 0
        while count < target:
            prev = value

            if i == len(nums1):
                value = nums2[j]
                j += 1
            elif j == len(nums2):
                value = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                value = nums1[i]
                i += 1
            else:
                value = nums2[j]
                j += 1

            count += 1

        if is_even:
            return (value + prev) / 2
        return value
