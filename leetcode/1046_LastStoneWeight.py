class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heapify(stones) # Max Heap

        while len(stones) > 2:
            biggest = self.pop(stones)
            second_biggest = self.pop(stones)

            remaining = biggest - second_biggest
            if remaining > 0:
                self.push(stones, remaining)

        if len(stones) > 1:
            return stones[1]
        return 0

    def heapify(self, stones: List[int]):
        stones.append(stones[0])
        stones[0] = None # We do not need the 0th element

        stones_size = len(stones) - 1
        middle_point = stones_size // 2

        index = middle_point
        while index > 0:
            self.percolate_down(stones, index)
            index -= 1
        
    def pop(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return None

        top = stones[1]
        if len(stones) > 2:
            stones[1] = stones.pop()
            self.percolate_down(stones, 1)
        else:
            stones.pop()

        return top

    def push(self, stones: List[int], value: int):
        stones.append(value)
        index = len(stones) - 1

        while index > 1 and stones[index] > stones[index // 2]:
            temp = stones[index // 2]
            stones[index // 2] = stones[index]
            stones[index] = temp

            index = index // 2

    def percolate_down(self, stones: List[int], index: int):
        current_stone = index
        while current_stone * 2 < len(stones):
            left_index = current_stone * 2
            right_index = current_stone * 2 + 1

            if right_index < len(stones) and stones[right_index] >= stones[left_index] and stones[right_index] > stones[current_stone]:
                temp = stones[right_index]
                stones[right_index] = stones[current_stone]
                stones[current_stone] = temp
                current_stone = right_index
            elif stones[left_index] > stones[current_stone]:
                temp = stones[left_index]
                stones[left_index] = stones[current_stone]
                stones[current_stone] = temp
                current_stone = left_index
            else:
                break