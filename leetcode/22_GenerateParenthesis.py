class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generator([], 0, 0, n, result)
        return result


    def generator(self, current: List[str], opened: int, closed: int, n: int, result: List[str]):
        if opened == n and closed == n:
            result.append(''.join(current))
            return

        if opened < n:
            current.append('(')
            self.generator(current, opened + 1, closed, n, result)
            current.pop()
        if opened > closed:
            current.append(')')
            self.generator(current, opened, closed + 1, n, result)
            current.pop()
