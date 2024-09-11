#!/usr/bin/env python3
"""no modules"""


def schools_by_topic(mongo_collection, topic):
    """find documents from collection"""
    return mongo_collection.find({"topics": topic})
