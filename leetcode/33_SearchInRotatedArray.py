class Solution:
    '''
    target = 5
     L     *     R
    [7,0,1,2,4,5,6]


    target = 0
     L     *     R
    [6,7,0,1,2,4,5]

    target = 0
     L     *     R
    [4,5,6,7,0,1,2]

    If L < R, use regular binary search:
        If middle is smaller than the target, move to right
        If middle is greater than the target, move to left
    Else:
        pass
    '''
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[L] < nums[R]:
                if nums[mid] < target:
                    L = mid + 1
                elif nums[mid] > target:
                    R = mid - 1
                else:
                    return mid
            else:
                if nums[mid] < target:
                    if nums[mid] > nums[L] or nums[L] > target:
                        L = mid + 1
                    else:
                        R = mid - 1
                elif nums[mid] > target:
                    if nums[mid] < nums[R] or nums[R] < target:
                        R = mid - 1
                    else:
                        L = mid + 1
                else:
                    return mid

        return -1
