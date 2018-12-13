#!/usr/bin/python3
"""
module containing list_all function
"""


def list_all(mongo_collection):
    """ lists all documents in a collection """
    return [i for i in mongo_collection.find()]
