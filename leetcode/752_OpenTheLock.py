class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        START = '0000'
        set_deadends = set(deadends)
        visited = set()
        turns = 0
        queue = deque()

        queue.append(START)
        visited.add(START)

        if START in set_deadends:
            return -1

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return turns
                
                for i in range(len(current)):
                    c = int(current[i])
                    up = c + 1
                    if up > 9:
                        up = 0
                    turn_up = current[:i] + str(up) + current[i+1:]
                    if turn_up not in visited and turn_up not in set_deadends:
                        visited.add(turn_up)
                        queue.append(turn_up)

                    down = c - 1
                    if down < 0:
                        down = 9
                    turn_down = current[:i] + str(down) + current[i+1:]
                    if turn_down not in visited and turn_down not in set_deadends:
                        visited.add(turn_down)
                        queue.append(turn_down)

                    if turn_up == target or turn_down == target:
                        return turns + 1

            turns += 1

        return -1
