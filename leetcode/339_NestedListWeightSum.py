# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    '''
    Use a similar technique as BFS to visit each level of the lists
    1. Iterate the current list, if the value is an integer multiply it by the level and sum it
    2. If the value is another list, add it to a queue for the next iteration
    3. After visiting all the integers of the list, increase the level by 1
    4. Repeat until our queue is empty
    '''
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        result = 0

        queue = deque()
        queue.extend(nestedList)
        level = 1

        while queue:
            for _ in range(len(queue)):
                item = queue.popleft()
                if item.isInteger():
                    result += item.getInteger() * level
                else:
                    queue.extend(item.getList())
            level += 1

        return result
