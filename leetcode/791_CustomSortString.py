class Solution:
    '''
    1. Convert the order string to a set
    2. Create a new string to store the result
    3. Add to the new string every character that is not on the order string
    4. If the string is in order, store it on a hashmap and keep a count of how many times it is seen
    5. Then iterate the order String, if it is on the hashmap add the character to the result the number of times it was repeated
    '''
    def customSortString(self, order: str, s: str) -> str:
        result = ''
        ordered = set(order)
        count = defaultdict(int)

        for c in s:
            if c in ordered:
                count[c] += 1
            else:
                result += c

        for c in order:
            if c in count:
                result += c * count[c]

        return result
