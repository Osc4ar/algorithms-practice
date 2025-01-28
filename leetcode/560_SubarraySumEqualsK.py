class Solution:
    '''
    [-2, -3, -5, -2]

    {
        0: 0
        -2: 1,
        -3, 0,
        -5, 0,
    }

    [-2, -3, -5, 0]
    {
        0: 1
        -2: 0
        -3: 0
        -5: 0
    }

    [1, 3, 6]
    {
        3: 1,
        1: 0,
        6: 0
    }
    6 - target = 3

    1. Create a prefix sum of every position and store it with the index on a HashMap with a frequency of 1
    2. If the sum is equal to k increase our count by 1
    3. Get what we need to reach target, like this: current_sum - target
    4. If we have the difference on the hashmap, increase the count by the number of prefix sums with that value
    5. Add the current sum to the hashmap with a frequency of 1
    6. Return the count
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)

        count = 0
        current = 0
        for i, n in enumerate(nums):
            current += n

            if current == k:
                count += 1
            if current - k in sums:
                count += sums[current - k]
            
            sums[current] += 1

        return count
