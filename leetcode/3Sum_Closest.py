class Solution:
    '''
      *      L  R
    [-4, -1, 1, 2]
    current = 3
    target = 1 - (-4) = 5
    closest = -1
          *  L  R
    [-4, -1, 1, 2]
    target = 1 - (-1) = 2
    current = 3
    closest = abs(2 - 3)
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sort = sorted(nums)

        min_distance = float('inf')
        closest = None
        for i in range(len(sort) - 2):
            left = i + 1
            right = len(sort) - 1

            while left < right:
                s = sort[i] + sort[left] + sort[right]
                distance = abs(target - s)

                if distance == 0:
                    return s
                if distance < min_distance:
                    closest = s
                    min_distance = distance

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1

        return closest
