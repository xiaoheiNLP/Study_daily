# -*-coding:utf-8-*-
# @Time    : 2019/12/9 0009 15:09
# @Author  :zhu
# @File    : numba_3.py
# @task description :
from numba import vectorize, int64
import numpy as np
import time


img1 = np.ones((9000, ), np.int64)

img2 = np.zeros((9000, ), np.int64)


#
@vectorize([int64(int64, int64)], target='parallel')
def merge(a, b):
    return np.square(a+b)


timeStart = time.time()
for i in range(10000):
    merge(img1, img2)
print(time.time() - timeStart)
