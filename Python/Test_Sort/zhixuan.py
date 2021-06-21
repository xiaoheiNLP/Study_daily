# -*- coding: utf-8 -*-
# @Time    : 2019-06-14 14:14
# @Author  : xinquan
# @File    : zhixuan.py

from functools import wraps


def fib_direct(n):
    assert n > 0, 'invalid n'
    if n < 3:
        return n
    else:
        return fib_direct(n - 1) + fib_direct(n - 2)


def cache(func):
    caches = {}  # 使用dict来缓存

    @wraps(func)
    def wrap(*args):
        if args not in caches:
            caches[args] = func(*args)

        return caches[args]
    return wrap


@cache
def fib_cache(n):
    assert n > 0, 'invalid n'
    if n < 3:
        return 1
    else:
        return fib_cache(n - 1) + fib_cache(n - 2)


if __name__ == "__main__":
    from timeit import Timer
    t1 = Timer("fib_direct(10)", "from __main__ import fib_direct")
    t2 = Timer("fib_cache(10)", "from __main__ import fib_cache")

    print(t1.timeit(100000))
    print(t2.timeit(100000))

