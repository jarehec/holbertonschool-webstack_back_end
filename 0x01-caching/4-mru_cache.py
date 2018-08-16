#!/usr/bin/python3
"""
module containing MRUCache class
"""
from collections import Counter

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ mru caching system """
    def __init__(self):
        """ initializing """
        super().__init__()
        self.indexes = Counter()

    def put(self, key, item):
        """ add item to cache_data """
        if key is not None and item is not None:
            if len(self.indexes) == BaseCaching.MAX_ITEMS:
                tmp = max(self.indexes, key=self.indexes.get)
                print('DISCARD:', tmp)
                self.cache_data.pop(tmp)
                self.indexes.pop(tmp)
            if len(self.indexes) == 0:
                self.indexes[key] = 0
            else:
                self.indexes[key] = self.indexes[max(self.indexes,
                                                 key=self.indexes.get)] + 1
            self.cache_data[key] = item

    def get(self, key):
        """ get item from cache_data """
        if key is not None and self.indexes.get(key) is not None:
            self.indexes[key] = self.indexes[max(self.indexes,
                                             key=self.indexes.get)] + 1
            return self.cache_data.get(key)
