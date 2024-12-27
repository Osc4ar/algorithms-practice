class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((timestamp, value))
        else:
            self.dict[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        
        values = self.dict[key]
        if values[0][0] > timestamp:
            return ""

        left = 0
        right = len(values) - 1
        value = ""
        while left <= right:
            middle = (right + left) // 2
            if values[middle][0] > timestamp:
                right = middle - 1
            elif values[middle][0] < timestamp:
                value = values[middle][1] # we save the latest value in case we do not have other
                left = middle + 1
            else:
                return values[middle][1]
        
        return value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
