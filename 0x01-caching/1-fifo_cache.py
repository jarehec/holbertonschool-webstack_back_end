#!/usr/bin/python3
"""
module containing FIFOCache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifo caching system """
    def __init__(self):
        """ initializing """
        super().__init__()
        self.indexes = []

    def put(self, key, item):
        """ add item to cache_data """
        if key is not None and item is not None:
            if self.cache_data.get(key) is None:
                self.indexes.append(key)
            self.cache_data[key] = item
        if len(self.indexes) > BaseCaching.MAX_ITEMS:
            print('DISCARD:', self.indexes[0])
            self.cache_data.pop(self.indexes[0])
            self.indexes.pop(0)

    def get(self, key):
        """ get item from cache_data """
        if key is not None:
            return self.cache_data.get(key)
