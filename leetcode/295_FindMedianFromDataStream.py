'''
We need the numbers sorted to get the median in constant time
We could insert the numbers into an array using binary search O(log(n))
'''
class MedianFinder:

    def __init__(self):
        self.half1 = [] # Max heap, smaller elements
        self.half2 = [] # Min heap, greater elements

    def addNum(self, num: int) -> None:
        if len(self.half1) == 0:
            heapq.heappush(self.half1, -1*num)
            return

        if len(self.half2) == 0:
            if num > -1*self.half1[0]:
                heapq.heappush(self.half2, num)
            else:
                old_head = heapq.heappushpop(self.half1, -1*num)
                heapq.heappush(self.half2, -1*old_head)
            return
        
        if num > self.half2[0]:
            heapq.heappush(self.half2, num)
        else:
            heapq.heappush(self.half1, -1*num)

        diff = len(self.half1) - len(self.half2)
        if diff == 2:
            old_head = heapq.heappop(self.half1)
            heapq.heappush(self.half2, -1*old_head)
        elif diff == -2:
            old_head = heapq.heappop(self.half2)
            heapq.heappush(self.half1, -1*old_head)

    def findMedian(self) -> float:
        if len(self.half1) > len(self.half2):
            return -1*self.half1[0]
        if len(self.half1) < len(self.half2):
            return self.half2[0]
        
        median = (-1*self.half1[0] + self.half2[0]) / 2
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
