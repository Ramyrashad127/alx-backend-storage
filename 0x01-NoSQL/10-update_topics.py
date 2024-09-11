#!/usr/bin/env python3
"""no modules"""


def update_topics(mongo_collection, name, topics):
    """update documents from collection"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
