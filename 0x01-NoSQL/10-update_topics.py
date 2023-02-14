#!/usr/bin/env python3
"""
Updates a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates a document in the mongo_collection
    """
    mongo_collection.update_many(
        {"name": "name"}, {"$set": {"topics": topics}}, {"multi": True})
