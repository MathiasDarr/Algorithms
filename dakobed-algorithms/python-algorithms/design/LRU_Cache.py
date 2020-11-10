"""
LeetCode 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.


We can use an OrderdDictionary from collections

This dictionary will remember the order in which items were inserted into the dictionary
The move_to_end(key)

"""
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.size = capacity
        self.lru_cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        else:
            self.lru_cache.move_to_end(key)
            return self.lru_cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.lru_cache:
            if len(self.lru_cache) >= self.size:
                self.lru_cache.popitem(last=False)
        else:
            self.lru_cache.move_to_end(key)
        self.lru_cache[key] = value

