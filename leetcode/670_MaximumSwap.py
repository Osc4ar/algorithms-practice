class Solution:
    '''
    1. Store the number in an array, each digit is a cell. O(n)
    2. Use a max heap to get the max value from all the digits. O(n)
    3. Replace the first element by the max value, look for the max value in the list to make the swap
    4. Convert the list to a num and return
    '''
    def maximumSwap(self, num: int) -> int:
        num_list = [int(c) for c in list(str(num))]

        heap = []
        for n in num_list:
            heapq.heappush(heap, -1*n)

        i = 0
        swapped = None
        target = None
        while heap:
            max_digit = -1 * heapq.heappop(heap)
            if max_digit != num_list[i]:
                swapped = num_list[i]
                target = max_digit
                num_list[i] = target
                break
            i += 1

        for i in reversed(range(len(num_list))):
            if num_list[i] == target:
                num_list[i] = swapped
                break

        result = 0
        for i, n in enumerate(reversed(num_list)):
            result += n * 10**i

        return result
