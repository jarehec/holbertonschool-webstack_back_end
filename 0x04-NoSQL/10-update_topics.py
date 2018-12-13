#!/usr/bin/python3
"""
module containing update_topics function
"""


def update_topics(mongo_collection, name, topics):
    """ updates documents in the mongo_collection """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
