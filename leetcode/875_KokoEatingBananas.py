class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        if len(piles) == h:
            return max_k

        left = 1
        right = max_k
        k = max_k

        while left <= right:
            middle = (right + left) // 2

            # we can reduce middle if is still valid
            if self.is_valid_k(piles, h, middle):
                k = middle
                right = middle - 1
            # we have to increase middle if is not valid
            else:
                left = middle + 1

        return k

    def is_valid_k(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0

        for bananas in piles:
            current_hours = bananas // k
            if bananas % k > 0:
                current_hours += 1
            hours += current_hours

            if hours > h:
                return False

        return True
