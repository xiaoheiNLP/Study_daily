# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 10:37 下午
# @Author  : xinquan
# @File    : log_1.py

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)
    return wrapper


@log
def test(p):
    print(test.__name__ + " param: " + p)

if __name__ == '__main__':
    test("I'm a param")