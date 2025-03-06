class Solution:
    '''
    0. Save the result on a stack, if there is not collision simply add the elements to the stack
    1. We only have collision when the current asteroid is going to the left and the head of the stack to the right
    2. If we have a collision, calculate which is the winner asteroid
    3. If the negative asteroid is destroyed, we stop iterating and move to the next one
    4. If the positive asteroid is desotryed, we pop the positive asteroid and continue the collision
    5. Return the stack after all asteroids were verified
    '''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            destroyed = False
            while stack and (not destroyed) and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff == 0:
                    destroyed = True
                    stack.pop()
                elif diff > 0:
                    destroyed = True
                else:
                    stack.pop()

            if not destroyed:
                stack.append(a)

        return stack
