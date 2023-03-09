def climbStairs(n: int, current: int) -> int:
    if current == n:
        return 1
    
    if current > n:
        return 0
    
    if current is None:
        current = 0
    
    return climbStairs(n, current+1) + climbStairs(n, current+2)

print(climbStairs(6, 0))