#!/usr/bin/python3
"""
module containing schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """ searches for a topic in the mongo_collection """
    return mongo_collection.find({'topics': topic})
