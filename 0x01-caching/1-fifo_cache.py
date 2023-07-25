#!/usr/bin/env python3
"""
FIFO caching:
Create a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class:
    Create a class FIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                first = self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
