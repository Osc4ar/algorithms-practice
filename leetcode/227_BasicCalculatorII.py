class Solution:
    '''
    We may use two lists to store numbers and operations:
    Then we iterate the operators and execute all the '*' and '/' first
    then we iterate with the results and calculate '+' and '-'

    '3+2*2'
    3, 2, 2
    + *

    3 4
    +

    7


    '3+2*2+4'
    3, 2, 2, 4
    + * +
    '''
    def calculate(self, s: str) -> int:
        digits = '0123456789'
        operators = '+-/*'

        nums = []
        ops = []

        current = ''
        for c in s:
            if c in digits:
                current += c
            elif c in operators:
                nums.append(int(current))
                current = ''
                ops.append(c)

        nums.append(int(current))

        # Higher priority * and /
        ops_to_clear = []
        removed = 0
        for i in range(len(ops)):
            nums_i = i - removed
            if ops[i] == '*':
                nums[nums_i] = nums[nums_i] * nums[nums_i+1]
                nums.pop(nums_i+1)
                removed += 1
                ops_to_clear.append(i)
            elif ops[i] == '/':
                nums[nums_i] = nums[nums_i] // nums[nums_i+1]
                nums.pop(nums_i+1)
                removed += 1
                ops_to_clear.append(i)

        for i in reversed(ops_to_clear):
            ops.pop(i)

        # Lower priority + and -
        ops_to_clear = []
        removed = 0
        for i in range(len(ops)):
            nums_i = i - removed
            if ops[i] == '+':
                nums[nums_i] = nums[nums_i] + nums[nums_i+1]
                nums.pop(nums_i+1)
                removed += 1
                ops_to_clear.append(i)
            elif ops[i] == '-':
                nums[nums_i] = nums[nums_i] - nums[nums_i+1]
                nums.pop(nums_i+1)
                removed += 1
                ops_to_clear.append(i)

        return nums[0]
