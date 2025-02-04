class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        node.prev.next = node
        node.next.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        curr = self.nodeMap[key]
        self.remove(curr)
        self.insert(curr)
        return curr.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])
        self.nodeMap[key] = Node(key,value)
        self.insert(self.nodeMap[key])

        if len(self.nodeMap)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.nodeMap[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)