class Solution:
    '''
    1. Count the frequencies of every letter
    2. Sort them by frequency
    3. Start adding characters by frequency, every letter until we are done

    Issues: Sorting is O(n*log(n)), Adding characters by frequency might cause an issue if we have a character with a high freq


    Example:
    aaabc
    abaca

    We can improve this by instead of sorting, heapify the letters by frequency
    We can take one character, update its frequency reducing by one and then pushing the new count to the heap
    Until we are done with the characters
    '''
    def reorganizeString(self, s: str) -> str:
        freqs = Counter(s)
        heap = []

        for c, freq in freqs.items():
            heapq.heappush(heap, (-1*freq, c))

        result = ''
        while heap:
            freq, c = heapq.heappop(heap)

            if len(result) > 0 and result[-1] == c:
                if len(heap) == 0:
                    return ''

                second, c2 = heapq.heappop(heap)

                heapq.heappush(heap, (freq, c))
                freq = second
                c = c2

            result += c

            freq += 1
            if freq < 0:
                heapq.heappush(heap, (freq, c))

        return result
