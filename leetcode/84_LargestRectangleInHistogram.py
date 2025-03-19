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
        result = 0

        for i, height in enumerate(heights):
            index = i
            while stack and stack[-1][0] > height:
                max_height, index = stack.pop()
                area = max_height * (i - index)
                result = max(result, area)

            stack.append((height, index))
        

        for height, start in stack:
            area = height * (len(heights) - start)
            result = max(result, area)

        return result
