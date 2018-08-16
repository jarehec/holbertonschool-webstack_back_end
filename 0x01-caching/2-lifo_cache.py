#!/usr/bin/python3
"""
module containing LIFOCache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ lifo caching system """
    def __init__(self):
        """ initializing """
        super().__init__()
        self.indexes = []

    def put(self, key, item):
        """ add item to cache_data """
        if key is not None and item is not None:
            if self.cache_data.get(key) is None:
                self.indexes.append(key)
            else:
                self.indexes.remove(key)
                self.indexes.append(key)
            self.cache_data[key] = item
        if len(self.indexes) > BaseCaching.MAX_ITEMS:
            print('DISCARD:', self.indexes[BaseCaching.MAX_ITEMS - 1])
            self.cache_data.pop(self.indexes[BaseCaching.MAX_ITEMS - 1])
            self.indexes.pop(BaseCaching.MAX_ITEMS - 1)

    def get(self, key):
        """ get item from cache_data """
        if key is not None:
            return self.cache_data.get(key)
