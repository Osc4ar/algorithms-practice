'''
1. Keep a count of how many numbers we have saved and the sum of the total numbers in the window
2. Every time we add a number, we check if the number fits on the window
3. If it fits, add it to the window and the sum
4. If it does not fit, pop the first value on the window, remove it from the sum and add the new number
5. Return the sum / numbers
'''
class MovingAverage:

    def __init__(self, size: int):
        self.max_size = size
        self.sum = 0
        self.window = []

    def next(self, val: int) -> float:
        if len(self.window) == self.max_size:
            self.sum -= self.window.pop(0)

        self.sum += val
        self.window.append(val)
        
        return self.sum / len(self.window)
