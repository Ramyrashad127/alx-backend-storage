#!/usr/bin/env python3
"""no modules"""


def insert_school(mongo_collection, **kwargs):
    """insert documents from collection"""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
