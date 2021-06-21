# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 10:44 上午
# @Author  : xinquan
# @File    : cProfile_1.py



from decimal import *

def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s

exp(Decimal(150))
exp(Decimal(400))
exp(Decimal(3000))


