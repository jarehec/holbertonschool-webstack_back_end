#!/usr/bin/python3
"""
module containing BasicCache class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ basic caching """
    def put(self, key, item):
        """ put item in cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get item from cache_data """
        if key is not None:
            return self.cache_data.get(key)
