# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 11:06 下午
# @Author  : xinquan
# @File    : decotator_03.py



def w1(func):
    print('1')
    def inner():
        print('2')
        return func()+"1"
    return inner

def w2(func):
    print('4')
    def inner():
        print('5')
        return func()+"2"
    return inner

@w2
@w1
def f1():
    print(3)
    return "zhu"

# 执行f1
print(f1())
# 1 2 3 # 只有w1 装饰
# 1 4 5 2 3 # w1,w2共同装饰

# 不执行f1
# 1 4