#!/usr/bin/env python3
""" redis module"""

import redis
import uuid
from typing import Union


class Cache():
    """ cache class"""
    def __init__(self):
        """constructor for cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
