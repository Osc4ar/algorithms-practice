class Solution:
    '''
    Brute Force solution O(n^2)
    Get the minimum of the current array, substract it from the array
    Repeat the operation until all elements of the array are zero or the array is empty if you skip zero values


    Optimal solution O(n)
    1. Get the max from the array
    2. Remove any duplicate
    3. Add all the values on a min heap to get the smallest value in constant time
    4. Keep a sum of the min values, every time you pop a value add to it the difference between it and the current sum
    5. Repeat until the sum is greater than or equal to the max value 
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        target = max(nums)
        no_duplicates = list(set(nums))
        heapq.heapify(no_duplicates) # Linear time complexity

        if no_duplicates[0] == 0:
            heapq.heappop(no_duplicates)

        current = 0
        count = 0
        while current < target:
            step = heapq.heappop(no_duplicates) - current
            current += step
            count += 1

        return count
