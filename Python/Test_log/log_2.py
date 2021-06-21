# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 10:50 下午
# @Author  : xinquan
# @File    : log_2.py

import functools


def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_with_param("param")
def test_with_param(p1):
    print('注意1:', p1)
    # print('注意1:', p2)


if __name__ == '__main__':
    test_with_param("zhu")

