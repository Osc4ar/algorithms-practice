'''
Brute Force approach, O(n) memory and time complexities
1. Store the nums on an array
2. To calculate the dotProduct iterate both vectors using the same index
3. Accumulate the result of each product on a result

Optimizations:
We only care about values different than zero, so we might optimize space and time by
saving only the index different than zero on a HashMap, like this:

nums = [1, 0, 0, 2, 3]
hash = {
    0: 1,
    3: 2,
    4: 3
}

Then we only iterate the keys of the sparse vector, and multiple them against the other vector.
If the other vector does not have the key we can skip that product since we know it would be zero.
'''
class SparseVector:
    def __init__(self, nums: List[int]):
        self.hash = defaultdict(int)

        for i, n in enumerate(nums):
            if n != 0:
                self.hash[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        for k, n in self.hash.items():
            if k in vec.hash:
                result += n * vec.hash[k]

        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
