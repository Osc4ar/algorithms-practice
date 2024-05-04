class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                result = self.apply(left, right, token)
                stack.append(result)

        return stack.pop()

    def apply(self, left: int, right: int, operand: str) -> int:
        if operand == '+':
            return left + right
        if operand == '-':
            return left - right
        if operand == '*':
            return left * right
        if operand == '/':
            return int(left / right)
