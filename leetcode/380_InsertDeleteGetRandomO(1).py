class RandomizedSet:

    def __init__(self):
        self.items = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False

        self.items.append(val)
        self.positions[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False

        last = self.items.pop()
        target = self.positions[val]
        if target != len(self.items):
            self.positions[last] = target
            self.items[target] = last
        self.positions.pop(val)

        return True

    def getRandom(self) -> int:
        return sample(self.items, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
