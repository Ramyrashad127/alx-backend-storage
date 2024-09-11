#!/usr/bin/env python3
""" redis module"""

import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """ count calls for cache"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper to coubt"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """history decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapped fuction"""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper

class Cache():
    """ cache class"""
    def __init__(self):
        """constructor for cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
