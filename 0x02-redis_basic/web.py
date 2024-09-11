import requests
import redis
from typing import Optional


r = redis.Redis(host='localhost', port=6379, db=0)


def get_page(url: str) -> str:
    """retrive data"""
    count_key = f"count:{url}"
    r.incr(count_key)
    cache_key = f"cache:{url}"
    cached_content = r.get(cache_key)
    
    if cached_content:
        return cached_content.decode('utf-8')
    response = requests.get(url)
    page_content = response.text
    r.setex(cache_key, 10, page_content)
    
    return page_content
