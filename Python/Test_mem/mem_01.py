# -*-coding:utf-8-*-
# @Time    : 2019/6/12 0012 9:55
# @Author   :zhuxinquan
# @File    : mem_01.py
# 题目1 斐波那契数列
# 从第三项开始 每一项等于前两项的和 求第n项
# 1 1 2 3 5 8 13 21
from functools import wraps
import sys
sys.setrecursionlimit(100000)

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
    # print(n)
    assert n > 0, 'invalid n'
    if n < 3:
        return n
    else:
        return fib_cache(n - 1) + fib_cache(n - 2)


if __name__ == "__main__":
    from timeit import Timer

    # t1 = Timer("fib_direct(40)", "from __main__ import fib_direct")
    t2 = Timer("fib_cache(8000)", "from __main__ import fib_cache")

    # print(t1.timeit(1))
    print(t2.timeit(1))
