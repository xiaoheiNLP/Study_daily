# -*-coding:utf-8-*-
# @Time    : 2019/12/11 0011 18:06
# @Author  :zhu
# @File    : numpy_nan.py
# @task description :
import numpy as np

myarray = np.array([1, 2, np.nan])
# print(np.isnan(myarray).any())
# print(np.isnan(myarray))
# print()
print(myarray)
myarray[np.isnan(myarray)] = 0
print(myarray)

