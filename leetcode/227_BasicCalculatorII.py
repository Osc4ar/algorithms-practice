class Solution:
    '''
    We can use a stack to save pending items to calculate.
    1. If we have a digit, we add it to our current number
    2. If we find an operator we will check which operator is, based on that we will:
    3. If we have a * or /, we pop the previous value from the stack and do prev *operation* current, push the result onto the stack
    4. If we have a + or -, we store the value on the stack, if we have a - we store the negative number
    5. We will add every item on the stack when finished, therefore we can store negative numbers in case of substraction
    '''
    def calculate(self, s: str) -> int:
        digits = '0123456789'
        operators = '+-/*'

        pending = []
        current = ''
        prev_operator = '+'
        for c in s:
            if c in digits:
                current += c
            elif c in operators:
                num = int(current)

                if prev_operator == '+':
                    pending.append(num)
                elif prev_operator == '-':
                    pending.append(-1*num)
                elif prev_operator == '*':
                    prev = pending.pop()
                    pending.append(prev * num)
                elif prev_operator == '/':
                    prev = pending.pop()
                    if prev < 0:
                        res = abs(prev) // num
                        pending.append(-1 * res)
                    else:
                        pending.append(prev // num)
                
                prev_operator = c
                current = ''

        num = int(current)
        if prev_operator == '+':
            pending.append(num)
        elif prev_operator == '-':
            pending.append(-1*num)
        elif prev_operator == '*':
            prev = pending.pop()
            pending.append(prev * num)
        elif prev_operator == '/':
            prev = pending.pop()
            if prev < 0:
                res = abs(prev) // num
                pending.append(-1 * res)
            else:
                pending.append(prev // num)

        result = 0
        for n in pending:
            result += n

        return result
