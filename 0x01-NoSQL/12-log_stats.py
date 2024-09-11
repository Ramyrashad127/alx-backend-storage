#!/usr/bin/env python3
""" 
pymongo
"""


from pymongo import MongoClient


def log_stats():
    """ 
    new script with mongodb
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    total = logs_collection.count_documents({})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    path = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    get = logs_collection.count_documents({"method": "GET"})
    delete = logs_collection.count_documents({"method": "DELETE"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stats()
