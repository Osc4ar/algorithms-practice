class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        result = []

        for i, c in enumerate(s):
            if c != ')':
                result.append(c)

            if c == '(':
                count += 1
            elif c == ')' and count > 0:
                count -= 1
                result.append(c)

        for i in reversed(range(len(result))):
            if result[i] == '(' and count > 0:
                count -= 1
                result.pop(i)

        return ''.join(result)
