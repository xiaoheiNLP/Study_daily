# -*-coding:utf-8-*-
# @Time    : 2019/12/9 0009 14:26
# @Author  :zhu
# @File    : numba_2.py
# @task description :
import time
import numpy as np
from numba import vectorize, int64

num_loops = 50
img1 = np.ones((1000, 0), np.int64) * 5



img2 = np.ones((1000, 1000), np.int64) * 10
img3 = np.ones((1000, 1000), np.int64) * 15


@vectorize([int64(int64, int64, int64)], target='parallel')
def add_arrays(img1, img2, img3):
    return np.square(img1+img2+img3)


start1 = time.time()
for i in range(num_loops):
    result = add_arrays(img1, img2, img3)
end1 = time.time()
run_time1 = end1 - start1
print('Average time for normal numpy operation={}'.format(run_time1))

