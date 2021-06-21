# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 11:24 下午
# @Author  : xinquan
# @File    : decotator_04.py

def func(funName):
    print('1')
    def func_in(*args, **kwargs): # 形参
        print('2')
        funName(*args, **kwargs) # 调用传递参数
    return func_in


@func
def test(a, b):
    print('a=%d,b=%d'%(a, b))

test(10, 20)