class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = 0
        left = 0
        count = 0

        for right in range(len(arr)):
            if right - left + 1 > k:
                if current_sum / k >= threshold:
                    count += 1
                current_sum -= arr[left]
                left += 1

            current_sum += arr[right]

        if current_sum / k >= threshold:
            count += 1

        return count
