'''
We need the numbers sorted to get the median in constant time
We could insert the numbers into an array using binary search O(log(n))
'''
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        if len(self.data) == 0:
            self.data.append(num)
            return

        index = 0
        left = 0
        right = len(self.data) - 1
        while left <= right:
            middle = (left + right) // 2
            if num > self.data[middle]:
                index = max(index, middle+1)
                left = middle + 1
            elif num < self.data[middle]:
                right = middle - 1
            else:
                index = max(index, middle)
                break

        if index == len(self.data):
            self.data.append(num)
        else:
            self.data.insert(index, num)

    def findMedian(self) -> float:
        is_even = len(self.data) % 2 == 0
        middle = len(self.data) // 2

        if is_even:
            median = (self.data[middle] + self.data[middle - 1]) / 2
            return median

        return self.data[middle]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
