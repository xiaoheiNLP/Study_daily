# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 11:00 下午
# @Author  : xinquan
# @File    : decotator_02.py

def makeBold(fn):
    def warpped():
        print('1')
        return '<b>' + fn() + '</b>'
    return warpped

def makeItalic(fn):
    def warpped():
        print('2')
        return '<i>' + fn() + '</i>'
    return warpped

@makeBold
@makeItalic
def test1():
    print('3')
    return 'hello world'

ret = test1()
print(ret)

# 输出结果:
# 1
# 2
# 3
# <b><i>hello world</i></b>