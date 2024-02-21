class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generator('', 0, 0, n, result)
        return result


    def generator(self, current: str, opened: int, closed: int, n: int, result: List[str]):
        if opened == n and closed == n:
            result.append(current)
            return

        if opened < n:
            current += '('
            self.generator(current, opened + 1, closed, n, result)
            current = current[:-1]
        if opened > closed:
            current += ')'
            self.generator(current, opened, closed + 1, n, result)
            current = current[:-1]
