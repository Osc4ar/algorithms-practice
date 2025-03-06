class Solution:
    '''
    We can have two heaps: one min heap of size k to store the max values from the matrix
    Another heap of size limits[i] to store the max values from the ith row

    1. Iterate each row, for each row build a min heap of size limit[i]
    2. Also save the max of each row
    3. If the max is smaller than the head of the min heap, then move to the next row
    4. If the max is greater than the head of the min heap, add the elements on the heap while keeping its size k
    5. After visiting all rows, iterate all the values on the heap and save their value
    '''
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        if k == 0:
            return 0

        result = []
        for i, row in enumerate(grid):
            limit = limits[i]
            if limit == 0:
                continue

            current = []
            max_val = max(row)
            for val in row:
                if len(current) < limit:
                    heapq.heappush(current, val)
                elif val > current[0]:
                    heapq.heappushpop(current, val)
            
            if len(result) == k and max_val < result[0]:
                continue
 
            while len(result) < k and current:
                val = heapq.heappop(current)
                heapq.heappush(result, val)

            while current:
                val = heapq.heappop(current)
                if val > result[0]:
                    heapq.heappushpop(result, val)

        return sum(result)
