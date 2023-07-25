#!/usr/bin/env python3
""" Basic dictionary:
    Create a class BasicCache that inherits from
    BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class:
    Create a class BasicCache that inherits from
    BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
