#!/usr/bin/env python3
""" redis module"""

import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable[[bytes], any]] = None) -> Optional[any]:
        """base get method"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """convert o utf-8"""
        return self.get(key, lambda x: x.decode('utf-8') if x is not None else None)

    def get_int(self, key: str) -> Optional[int]:
        """convert to int"""
        return self.get(key, lambda x: int(x) if x is not None else None)
