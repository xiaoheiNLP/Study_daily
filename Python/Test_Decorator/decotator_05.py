# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 11:32 下午
# @Author  : xinquan
# @File    : decotator_05.py

from time import ctime, sleep

def timefun_arg(pre="hello"):
    def timefun(func):
        def warppedfunc():
            print('%s called at %s %s'%(func.__name__, ctime(), pre))
            return func()
        return warppedfunc
    return timefun


@timefun_arg('it') # 执行，主动调用。需要多一层闭包函数
def foo():
    print('foo')
#
@timefun_arg('Python')
def too():
    print('too')

# foo()
# sleep(2)
too()