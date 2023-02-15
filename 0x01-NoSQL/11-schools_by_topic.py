#!/usr/bin/env python3
"""
Returns a matching document
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a document that has the topic provided
    """
    return list(mongo_collection.find({"$in": {"topics": topic}}))
