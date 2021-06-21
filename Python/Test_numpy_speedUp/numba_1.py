# -*-coding:utf-8-*-
# @Time    : 2019/12/9 0009 14:09
# @Author  :zhu
# @File    : numba_1.py
# @task description :

from numba import jit
import time
import random

num_loops = 50
len_of_list = 10000

# @jit(nopython=True)
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # 从后往前对比，从小到大排序
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # 找到当前元素的位置
        arr[pos] = cursor
    return arr


list_of_numbers = list()
for i in range(len_of_list):
    num = random.randint(0, len_of_list)
    list_of_numbers.append(num)


start = time.time()
for i in range(num_loops):
    result = insertion_sort(list_of_numbers)

end = time.time()

run_time = end-start
print('Average time={}'.format(run_time))
