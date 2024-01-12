class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            if not len(stack):
                stack.append((t, index))
                continue

            top, top_index = stack[-1]

            if t <= top:
                stack.append((t, index))
                continue

            while t > top and len(stack):
                top, top_index = stack.pop()
                results[top_index] = index - top_index

                if len(stack):
                    top, top_index = stack[-1]

            stack.append((t, index))

        return results
