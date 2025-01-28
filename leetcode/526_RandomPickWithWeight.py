class Solution:
    '''
    One option is to duplicate the values based on their weight, if we have a list of weights: [1, 3] we could have an array: [0, 1, 1, 1]
    The issue with this approach is that we can receive a big number of weights and the array of indices would be extremely big

    Another option would be to have a "map" to know that every valueb below 0.25 is 0 and everything else is 1
    Something like:
    [0.25, 1]

    If we get a random number between 0 and 1, we can then iterate this array of weights and return the index
    where the random number is smaller than the value. To pick an index this would be linear time if we go value by value.
    But we can optimize this search by using binary search and start at the middle of the array.
    '''
    def __init__(self, w: List[int]):
        total = sum(w)
        self.probability = []
        prev = 0
        for weight in w:
            current = prev + weight / total
            self.probability.append(current)
            prev = current

    def pickIndex(self) -> int:
        picked = random.random()
        left = 0
        right = len(self.probability) - 1

        index = float('inf')
        while left <= right:
            middle = (right + left) // 2
            if self.probability[middle] >= picked:
                index = min(index, middle)
                right = middle - 1
            elif self.probability[middle] < picked:
                left = middle + 1

        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
