#!/usr/bin/env python3
"""no modules"""


def list_all(mongo_collection):
    """list all documents from collection"""
    return mongo_collection.find()
