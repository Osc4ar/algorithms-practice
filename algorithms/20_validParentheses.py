class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        brackets_stack = []

        for bracket in s:
            is_opening_bracket = bracket not in bracket_pairs

            if is_opening_bracket:
                brackets_stack.append(bracket)
            elif len(brackets_stack) > 0:
                actual_opening_bracket = brackets_stack.pop()
                expected_opening_bracket = bracket_pairs[bracket]
                is_matching_bracket = actual_opening_bracket == expected_opening_bracket

                if not is_matching_bracket:
                    return False
            else:
                return False

        return len(brackets_stack) == 0
