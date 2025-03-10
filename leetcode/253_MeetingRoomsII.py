class Solution:
    '''
    1. Sort the meeting intervals by their start time on increasing order
    2. Save on a min heap the end time of the meetings, starting for the first one
    3. For every meeting interval, check if the start time is bigger than the end time
    4. If it is bigger, then we can pop from the queue and push the end of the current meeting
    5. If it is not bigger, we push the end of the current meeting
    6. The size of the heap will have the number of meeting rooms needed
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_meetings = sorted(intervals)
        rooms = []
        heapq.heappush(rooms, sorted_meetings[0][1])

        for i in range(1, len(sorted_meetings)):
            start, end = sorted_meetings[i]

            if start >= rooms[0]:
                heapq.heappushpop(rooms, end)
            else:
                heapq.heappush(rooms, end)

        return len(rooms)
