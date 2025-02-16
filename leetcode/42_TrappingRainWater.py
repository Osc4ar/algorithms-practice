class Solution:
    '''
    We can trap water if:
    1. The current cell is smaller than the previous and next ones
    2. We can start at the left with a window whenever we have a value greater than zero
    3. The height is equal to the current value minus the container's edge. We always keep the smallest container's edge.

    We cannot trap water if:
    1. The cell is on the edges, either the first and last cells
    2. If we find an edge equal or taller than the initial edge, that indicates that section ends there.
    3. That new edge will be the left pointer, and we will keep looking as previously

    trapped = 3
    max_height = 1
     L       R
    [1,0,0,0,1]
    '''
    def trap(self, height: List[int]) -> int:
        prefix = []
        max_prefix = float('-inf')
        for h in height:
            if h > max_prefix:
                max_prefix = h
            prefix.append(max_prefix)

        suffix = []
        max_suffix = float('-inf')
        for h in reversed(height):
            if h > max_suffix:
                max_suffix = h
            suffix.append(max_suffix)
        suffix = suffix[::-1]

        trapped = 0
        for i, h in enumerate(height):
            container = min(prefix[i], suffix[i])
            diff = container - h
            trapped += diff

        return trapped
