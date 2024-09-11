#!/usr/bin/env python3
"""
no modules
"""


def top_students(mongo_collection):
    """ new function python """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
