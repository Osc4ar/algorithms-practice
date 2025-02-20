class Solution:
    '''
    We can reach the end as long as we have values different than zero in the path
    If we have a value equal to zero, we could reach the end if we have a wait to avoid the index of the zero value

    1. Iterate the array once, identify all the zeroes and their indexes
    2. If there are not zeroes, return True
    3. If there are zeroes, start checking the array again
    4. If the value + its index is bigger than the first zero index, we move to the next zero index
    5. Repeat until we reach the end or a zero index is bigger than the index we have
    6. If we did not reach the end, we continue at the zero index + 1 to check the values
    7. If we do not find any value which can jump the zero before reaching the zero, return False
    
        Z
    [1, 3]
         I
       *   *
    [2,0,2,0,1,4]
    '''
    def canJump(self, nums: List[int]) -> bool:
        zeroes = []
        for i, n in enumerate(nums):
            if n == 0:
                zeroes.append(i)

        if len(nums) == 1 or len(zeroes) == 0:
            return True
        if len(nums) == len(zeroes):
            return False

        i = 0
        z = 0
        max_jump = -1
        while z < len(zeroes):
            if i == zeroes[z] and max_jump == -1:
                return False
            elif i == zeroes[z]:
                i = max_jump
                max_jump = -1

            new_index = i + nums[i]
            if new_index >= len(nums) - 1:
                return True

            if new_index > zeroes[z]:
                while z < len(zeroes) and new_index > zeroes[z]:
                    z += 1
                if z == len(zeroes):
                    return True
                max_jump = max(max_jump, zeroes[z-1])
            i += 1
        
        return True
