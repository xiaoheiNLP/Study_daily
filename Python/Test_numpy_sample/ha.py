# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 11:30 下午
# @Author  : xinquan
# @File    : ha.py
import numpy as np


rand_arr = np.random.random((5, 3))
print(rand_arr)
print()

# Create the random array
rand_arr = np.random.random([5, 3])
print(rand_arr)
print()

# Limit to 3 decimal places
np.set_printoptions(precision=2)
t = rand_arr
print(t)


a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
doublediff = np.diff(np.sign(np.diff(a)))
peak_locations = np.where(doublediff == -2)[0] + 1
print(peak_locations)


print()


a_2d = np.array([[3, 3, 3], [4, 4, 4], [5, 5, 5]])
b_1d = np.array([1, 2, 3])
print(b_1d[:, None])
print(a_2d - b_1d[:, None])

print("*"*89)
import numpy as np
a = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]])
print('0维为None:')
print(a[None, 0:4])
print('1维为None:')
print(a[:,None])
