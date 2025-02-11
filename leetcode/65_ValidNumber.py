class Solution:
    '''
    We could 'separate' the evaluation of the string by every rule
    1. First we check if we have a valid integer
    2. It would be valid if we have a sign (+, -), a digit or a point/period
    3. After that start we would have three valid next things: a digit, a point, an e, any other thing would return false
    4. If we find a point, we do not expect any other sign or period, but e is still valid
    5. If we find an e, we expect to find a sign or a digit, but no more 'e' nor points 
    '''
    def isNumber(self, s: str) -> bool:
        digits = '0123456789'
        signs = '+-'
        point = True
        sign = True
        e = False
        valid = False

        has_digits = False
        e_count = 0
        point_count = 0

        for c in s:
            if c in digits:
                has_digits = True

                sign = False
                e = e_count < 1
                point = e and point_count < 1
                valid = True
            elif c in signs:
                if not sign:
                    return False

                point = point_count < 1
                sign = False
                e = False
                valid = False
            elif c == '.':
                if not point:
                    return False
                point_count += 1

                point = False
                sign = False
                e = has_digits and e_count < 1
                valid = valid
            elif c == 'e' or c == 'E':
                if not e:
                    return False
                e_count += 1

                point = False
                sign = True
                e = False
                valid = False
            else:
                return False
        
        return valid
