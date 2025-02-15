class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    '''
    1. To store the key-values we can use a hash map/dictionary with O(1) put and get
    2. To keep track of the LRU key we might use a queue, the issue of the queue is when we read a value in the middle of it
    3. To optimize this we can use a double linked list, and keep a reference of every node on the dictionary
    4. When we insert a new value, we add a new Node to the linked list at the end of it
    5. When we reach the capacity we remove the left-most node from the cache and the linked list
    6. Any time we read or update a key, we move that node to the right-most position to know the Most Recently Used node
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.prev = self.left.next = self.right
        self.right.prev = self.right.next = self.left

    def append(self, node: Node):
        prev = self.right.prev
        self.right.prev = prev.next = node
        node.prev = prev
        node.next = self.right

    def remove(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.append(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)

        self.append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
