# -*-coding:utf-8-*-
# @Time    : 2019/6/6 0006 17:47
# @Author   :zhuxinquan
# @File    : men_02.py
import os, sys
import pip
print(pip.pep)
exit()


from functools import wraps
import numpy as np

def direct_compu(x):
    return x+100*30/2


def cache(func):
    cache_dict = {}

    @wraps(func)
    def wrap(value):
        key = value  # 函数参数作为key(请保证用参数构成的key可哈希)
        if key not in cache_dict:
            cache_dict[key] = func(value)
            print(key, func(value), '被缓存')
        return cache_dict[key]
    return wrap


@cache
def cached_compu(x):
    return x+100*30/2


if __name__ == '__main__':
    import time
    num_list = np.random.randint(1, 5, int(1e7))
    print(num_list)
    exit()
    begin_time1 = time.time()
    result1 = [direct_compu(num) for num in num_list]
    end_time1 = time.time()

    begin_time2 = time.time()
    result2 = [cached_compu(num) for num in num_list]
    end_time2 = time.time()

    print('result1 time: %s' % (end_time1-begin_time1))
    print('result2 time: %s' % (end_time2-begin_time2))

