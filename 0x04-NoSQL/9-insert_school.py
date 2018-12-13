#!/usr/bin/python3
"""
module containing insert_school function
"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a document into the mongo_collection """
    return str(mongo_collection.insert(kwargs))
