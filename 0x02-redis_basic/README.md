# 0x02. Redis Basics

## Description
This module explores **Redis**, an in-memory key-value data structure store used as a database, cache, and message broker. It covers basic caching patterns, atomic operations, function call metrics tracking, and web scraping cache systems with TTL (Time To Live).

## Learning Objectives
- Initializing the Redis client and interacting with Redis strings and lists.
- Storing and retrieving typed data (integers, strings, byte-arrays, JSON).
- Implementing decorators in Python to track function call counts and parameter history.
- Implementing an expiring web request cache using `redis-py` and `requests`.

## Tasks Summary

| File | Description |
| :--- | :--- |
| `exercise.py` | `Cache` class with `store(data)` using UUID keys, typed retrieval `get()`, `get_str()`, `get_int()`. Includes `count_calls` decorator tracking invocations via `INCR`, and `call_history` decorator storing inputs and outputs via `RPUSH`. |
| `web.py` | `get_page(url)` function fetching HTML with `requests`, caching HTML with 10-second expiration (`SETEX`), and tracking access count. |

## Author
- **Ramy Rashad** - [GitHub](https://github.com/Ramyrashad127)
