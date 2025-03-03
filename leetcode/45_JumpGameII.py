class Solution:
    '''
    We can solve this problem using a BFS iteration of the array as follows:
    1. Keep the elements we can reach on a queue, to avoid duplicates we can save the visited positions on a set
    2. While we have not reached the last value, increase the number of jumps by one for each visited level
    3. Pop elements of the current level, add to the queue the elements you can reach from that position
    4. If an element has been already added to the queue, we can skip it to avoid duplicates
    5. As soon as we reach the n-1 index, return the number of jumps
    '''
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        queue = deque()
        visited = set()

        queue.append(0)
        visited.add(0)

        jumps = 0
        while queue:
            jumps += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                for j in range(1, min(i+nums[i]+1, len(nums))):
                    if j == len(nums) - 1:
                        return jumps
                    if j not in visited:
                        queue.append(j)
                        visited.add(j)

        return jumps
