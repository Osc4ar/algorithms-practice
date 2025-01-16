class Solution:
    '''
    1. We can start with a container with the biggest distance from start to finish
    2. To maximize the size of the container, we can move the pointer of the smallest line
    3. We save the max container and keep iterating until the pointers meet at the middle
    4. We return the max container we found
    '''
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
