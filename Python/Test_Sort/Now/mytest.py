# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 13:45
# @Author  : xinquan
# @File    : mytest.py

import numpy as np

# def fib_recur(n):
#   if n <= 1:
#     return n
#
#   return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    np.random.seed(0)
    print(np.random.permutation(10))


