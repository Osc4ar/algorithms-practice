class Solution:
    '''
    We only care about the max value on the right so we can save it
    1. Iterate the array in reverse order
    2. Check if the current height is taller than the max height
    3. If it is taller, update the max height to the current height and add the index to the result
    4. By definition the right-most building has ocean view
    '''
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_height = float('-inf')

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]

        return result[::-1]
