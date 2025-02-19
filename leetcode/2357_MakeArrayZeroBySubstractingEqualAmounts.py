class Solution:
    '''
    We can say that every non-zero value is a step to reach a list full of zeroes
    It does not matter if we have duplicate values because we can do the operation to all values

    Therefore we only need to count the number of unique non-zero values, for that we can use a set 
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        uniques = set(nums)

        if 0 in uniques:
            uniques.remove(0)

        return len(uniques)
