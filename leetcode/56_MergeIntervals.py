class Solution:
    '''
    Brute force approach O(n^2):
    1. Iterate all the intervals, create a new one for the merged ones
    2. For every interval, check if there is a merged interval where this interval overlaps
    3. If an interval overlaps, keep the minimum from that interval and keep the maximum on the merged interval
    4. Keep doing this until we finished the iteration


    Sorting the intervals:
    1. We can sort the intervals O(n*log(n))
    2. Iterate the intervals and keep two variables, the current interval's start and end
    3. Check if the current start of the value is less than or equal than the end
    4. If they overlap, update the end variable to point to the new interval's end
    5. If they do not overlap, save the new merged interval on the result and update the variables
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        sorted_intervals = sorted(intervals)

        prev_start, prev_end = sorted_intervals[0]
        for start, end in sorted_intervals:
            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                result.append([prev_start, prev_end])
                prev_start = start
                prev_end = end

        result.append([prev_start, prev_end])

        return result
