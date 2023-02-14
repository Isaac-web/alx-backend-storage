#!/usr/bin/env python3
"""
Insert a new document into the collection provided
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the mongo_collection
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
