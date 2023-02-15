#!/usr/bin/env python3
"""
Updates a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    update many documents that match the
    name provided
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
