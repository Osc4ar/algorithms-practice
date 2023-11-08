class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest_numbers = [None] # Min Heap of the largest numbers in Stream
        self.k = k
        self.nums = nums

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        max_heap_size = self.k + 1
        if len(self.largest_numbers) == max_heap_size: # We insert in the top if Max Size is reached
            if val > self.get_top():
                self.push_top(val)
        else:
            self.push_heap(val)

        #self.nums.append(val)

        return self.get_top()

    # Pushes an element to the top of the heap, then orders it
    def push_top(self, val: int):
        index = 1
        self.largest_numbers[index] = val

        smallest_child, new_index = self.get_smallest_child(index)

        while new_index > 0 and index < len(self.largest_numbers):
            if val > smallest_child:
                self.largest_numbers[new_index] = val
                self.largest_numbers[index] = smallest_child

                index = new_index
                smallest_child, new_index = self.get_smallest_child(index)
            else:
                break


    def get_smallest_child(self, index):
        left = self.get_left(index)
        left_index = index * 2
        right = self.get_right(index)
        right_index = index * 2 + 1

        if left is None and right is None:
            return (None, 0)
        if left is None:
            return (right, right_index)
        if right is None:
            return (left, left_index)
        if left <= right:
            return (left, left_index)

        return (right, right_index)

    
    def get_left(self, index):
        left_index = index * 2

        if left_index < len(self.largest_numbers):
            return self.largest_numbers[left_index]
        return None

    def get_right(self, index):
        right_index = index * 2 + 1

        if right_index < len(self.largest_numbers):
            return self.largest_numbers[right_index]
        return None
    
    # Pushes an element to the end of the heap, then orders it
    def push_heap(self, val: int):
        self.largest_numbers.append(val)
        
        index = len(self.largest_numbers) - 1
        parent_index = index // 2

        while parent_index > 0:
            if self.largest_numbers[index] < self.largest_numbers[parent_index]:
                temp = self.largest_numbers[parent_index]
                self.largest_numbers[parent_index] = self.largest_numbers[index]
                self.largest_numbers[index] = temp

                index = parent_index
                parent_index = index // 2
            else:
                break

    def get_top(self):
        if len(self.largest_numbers) == 1:
            return self.largest_numbers[0]

        return self.largest_numbers[1]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)