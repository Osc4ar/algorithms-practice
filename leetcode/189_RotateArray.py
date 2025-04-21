class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        1. Reverse the whole array, in this way we will have the numbers on the portion of the array we want
        2. Reverse the first k elements of the reversed array
        3. Reverse the rest of the array elements
        """
        real_k = k % len(nums)

        # Whole array
        left = 0
        right = len(nums) - 1
        self.reverse_in_place(nums, left, right)

        # First k elements
        left = 0
        right = real_k - 1
        self.reverse_in_place(nums, left, right)

        # Rest of the array
        left = real_k
        right = len(nums) - 1
        self.reverse_in_place(nums, left, right)

    def reverse_in_place(self, nums, left, right):
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp

            right -= 1
            left += 1
