# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 10:32 下午
# @Author  : xinquan
# @File    : decotator_01.py


def MethodDecoration(function):  # 外层decorator
    c=150
    d=200
    def wrapper(a, b):            # 内层wrapper。和add_function参数要一样
        result=function(a, b)
        result=result*c/d        # 加密，相当于添加额外功能
        return result            # 此处一定要返回值
    return wrapper

@MethodDecoration
def add_function(a, b):
    return a+b

result=add_function(100,300)    #函数调用
print(result)