# 1 Реалізувати LFU алгоритм для кешування.
# За базу берем існуючий декоратор.Написати для фетчування юерелів.
# Додати можливість указати максимум елементів в кеші.
# 2 Створити декоратор для заміру пам'яті.


import functools
from collections import OrderedDict

import requests

import tracemalloc

max_limit = int(input('Enter maximum limit elements: '))


def cache(max_limit):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._usage_counter[cache_key] += 1
                return deco._cache[cache_key]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                least_used_key = min(deco._usage_counter, key=deco._usage_counter.get)
                del deco._cache[least_used_key]
                del deco._usage_counter[least_used_key]

            deco._cache[cache_key] = result
            deco._usage_counter[cache_key] = 1
            return result

        deco._cache = OrderedDict()
        deco._usage_counter = {}
        return deco

    return internal


def measure_memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        result = func(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")

        print(f"Memory usage of {func.__name__}:")
        for stat in top_stats[:5]:
            print(stat)

        return result

    return wrapper


@measure_memory_usage
@cache(max_limit)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

