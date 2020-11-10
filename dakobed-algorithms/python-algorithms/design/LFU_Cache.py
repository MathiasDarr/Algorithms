"""
LeetCode 460 LFU Cache
Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

    LFUCache(int capacity) Initializes the object with the capacity of the data structure. int get(int key) Gets the
    value of the key if the key exists in the cache. Otherwise, returns -1. void put(int key, int value) Sets or
    inserts the value if the key is not already present. When the cache reaches its capacity, it should invalidate
    the least frequently used item before inserting a new item. For this problem, when there is a tie (i.e.,
    two or more keys with the same frequency), the least recently used key would be evicted.


KeyFreq represents a dictionary that maps key to frequency
freqkeys dict represents a dict that maps one freq to many keys and these 'many keys' are stored in OrderedDict
that maps one freq to many keys, and many keys are stored in OrderDict

https://leetcode.com/problems/lfu-cache/discuss/369104/Python-two-dicts-explanation

"""
from collections import OrderedDict, defaultdict

class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.minfreq = None
        self.keyfreq = {}
        self.freqkeys = defaultdict(OrderedDict)


    def get(self, key):
        pass
    def put(self, key, value):
        pass