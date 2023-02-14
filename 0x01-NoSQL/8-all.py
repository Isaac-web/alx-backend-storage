#!/usr/bin/env python3
"""
List all the documents in a collection
"""


def list_all(mongo_collection):
    """
    Returns a list of documents in the mongo_collection or an
    empty list
    """
    result = mongo_collection.find()
    if not result:
        return []
    else:
        return list(result)
