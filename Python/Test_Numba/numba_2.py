# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 10:48 下午
# @Author  : xinquan
# @File    : numba_2.py


import time
import random
from numba import jit

num_loops = 50
len_of_list = 10000

@jit(nopython=True)
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > cursor:
            # 从后往前对比，从小到大排序
            arr[pos] = arr[pos-1]
            pos = pos-1
        # 找到当前元素的位置
        arr[pos] = cursor
    return arr
start = time.time()
list_of_numbers = list()
for i in range(len_of_list):
    num = random.randint(0, len_of_list)
    list_of_numbers.append(num)

for i in range(num_loops):
    result = insertion_sort(list_of_numbers)

end = time.time()

run_time = end-start
# print('Average time={}'.format(run_time/num_loops))
print('Average time={}'.format(run_time))