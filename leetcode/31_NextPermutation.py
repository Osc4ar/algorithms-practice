class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        decreasing = None
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            if nums[i] < nums[i+1]:
                decreasing = i
                break

        if decreasing is None:
            self.reverse(nums, 0)
            return

        closest = None
        for i in range(len(nums) - 1, decreasing, -1):
            if nums[i] > nums[decreasing]:
                closest = i
                break

        self.swap(nums, decreasing, closest)
        self.reverse(nums, decreasing + 1)

    def swap(self, nums, i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def reverse(self, nums, start: int):
        i = start
        j = len(nums) - 1

        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
