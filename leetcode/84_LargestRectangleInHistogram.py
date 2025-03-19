class Solution:
    '''
    1. Create a monotonic stack of increasing consecutive values
        a. To build the stack, check if the current value is bigger than the last value in the stack
        b. If it is not bigger, skip it but mark it as non-consecutive
        c. If a bigger value is found and non-consecutive is true, empty the stack checking the areas of the histograms
        d. Insert the new value and repeat for the whole list
    2. After building it, start popping from the bottom of the stack and keep the max value of:
        Popped Value * (len(stack) + 1)
    3. Return the max value of that operation as the result
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append((heights[0], 0))

        result = min(heights) * len(heights)

        for i in range(1, len(heights)):
            last_popped_index = float('inf')
            while stack and stack[-1][0] > heights[i]:
                max_height, index = stack.pop()
                area = max_height * (i - index)
                last_popped_index = index
                result = max(result, area)

            stack.append((heights[i], min(i, last_popped_index)))
        

        while stack:
            max_height, index = stack.pop()
            area = max_height * (len(heights) - index)
            result = max(result, area)

        return result
