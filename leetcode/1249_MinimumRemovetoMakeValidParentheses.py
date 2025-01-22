class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = []

        for i, c in enumerate(s):
            if c != ')':
                result.append(c)

            if c == '(':
                stack.append(c)
            elif c == ')' and len(stack) > 0:
                stack.pop()
                result.append(c)

        for i in reversed(range(len(result))):
            if result[i] == '(' and len(stack) > 0:
                stack.pop()
                result.pop(i)

        return ''.join(result)
