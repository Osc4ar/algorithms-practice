class Solution:
    '''
    1. Have two pointers, one for each list
    2. Compare the two intervals, for the one with the biggest start check:
        a. If its start is smaller than the end of the other interval
        b. If it is, insert a new intersection with [max(start), min(end)]
    3. Move the pointer of the list with the smallest end to the next interval
    '''
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        result = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]

            if first[0] >= second[0] and first[0] <= second[1]:
                result.append([first[0], min(first[1], second[1])])
            elif second[0] >= first[0] and second[0] <= first[1]:
                result.append([second[0], min(first[1], second[1])])

            if first[1] >= second[1]:
                j += 1
            else:
                i += 1

        return result
