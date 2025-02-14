class Solution:
    '''
    We cannot simply return the max value, because we can have the max value as the sum of the special numbers
    The difficult part is that the special numbers can be in any order and they are not always positive
    If the numbers were positive maybe we could use a heap and keep the two biggest numbers, it is really likely
    that the first or second numbers would be the outlier
    If we have negative numbers we have two scenarios:
    1. If there's a single negative: That's the outlier because is impossible to get a negative by suming positive numbers
    2. If there's more than one: It's likely the non-negative number is the outlier

    The sum of the array without the outlier would be 2 times the sum of the special numbers, if we get the sum of the array and then remove the element from it, we can discard any odd number, since the sum has to be even.

    If the number is even, we can divide the sum by 2, and check if it exists on the elements by using a hashmap or hash set

    Sum of array: 20
    [2,3,5,10]
    [18, 17, 15, 10]

    1. Get the sum of the array
    2. Count how many times every element appears on the array using a Hash Map
    3. Iterate every element once again, get the sum without that element
    4. Check if that sum is even, if it is divided it by 2
    5. Check if that number exists in our hashmap, if it does then the current number is the outlier
    6. There's an edge case when the potential sum element is the current element, if that is the case we do not have an outlier

    [-2,-1,-3,-6,4]
    Sum: -8
    [-6, -7, -5, -2, -12]

    Sum: 39
    [6,-31,50,-35,41,37,-42,13]
    [33, 70, -11, 74, -2, ]
    '''
    def getLargestOutlier(self, nums: List[int]) -> int:
        count = Counter(nums)
        total = sum(nums)

        outlier = float('-inf')
        for n in nums:
            new_total = total - n
            if new_total % 2 == 0:
                potential = new_total // 2
                if potential in count:
                    if n == potential and count[potential] == 1:
                        continue
                    else:
                        outlier = max(outlier, n)

        return outlier
