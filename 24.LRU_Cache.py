'''
Day 24 - 30 days Leetcoding Challenge - April 24, 2020

Problem (leetcode: 146)

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.deque = deque()
        
    def find(self, key: int) -> int:
        for i in range(len(self.deque)):
            n = self.deque[i]
            if n[0] == key:
                return i
        return -1
        

    def get(self, key: int) -> int:
        index = self.find(key)
        if index == -1:
            return -1
        else:
            k, v = self.deque[index]
            del self.deque[index]
            self.deque.append((k,v))
            return v
        

    def put(self, key: int, value: int) -> None:
        index = self.find(key)
        if index == -1:
            if len(self.deque) >= self.size:
                self.deque.popleft()
            self.deque.append((key, value))
        else:
            del self.deque[index]
            self.deque.append((key,value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
