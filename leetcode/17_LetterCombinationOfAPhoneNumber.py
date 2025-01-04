class Solution:
    '''
    1. Create a dictionary, the keys are the numbers and the values are the letter in a set for quick searching
    2. For every digit, add the first letter and then call the function again with the next digit.
    3. Repeat 2 until we do not have more digits to add, once we reached an end, we add the combination to a result's array
    4. We remove the current digit we are using and add the next one
    5. We repeat until we finish all recursive call backs, and return the results
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        digits2letters = {
            '2': {'a', 'b', 'c'},
            '3': {'d', 'e', 'f'},
            '4': {'g', 'h', 'i'},
            '5': {'j', 'k', 'l'},
            '6': {'m', 'n', 'o'},
            '7': {'p', 'q', 'r', 's'},
            '8': {'t', 'u', 'v'},
            '9': {'w', 'x', 'y', 'z'},
        }

        results = []

        def backtracking(subdigits: str, result: str):
            if subdigits == '':
                results.append(result)
                return

            digit = subdigits[0]
            for letter in digits2letters[digit]:
                result += letter
                backtracking(subdigits[1:], result)
                result = result[:-1]

        if digits == '':
            return []

        backtracking(digits, '')
        return results
