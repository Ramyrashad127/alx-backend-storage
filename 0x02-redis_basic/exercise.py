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

def replay(fn: Callable) -> None:
    """replay redis history."""
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    fn_name = fn.__qualname__
    in_key = '{}:inputs'.format(fn_name)
    out_key = '{}:outputs'.format(fn_name)
    fxn_call_count = 0
    if redis_store.exists(fn_name) != 0:
        fxn_call_count = int(redis_store.get(fn_name))
    print('{} was called {} times:'.format(fn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            fn_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))

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
