# -*-coding:utf-8-*-
# @Time    : 2019/12/18 0018 10:47
# @Author  :zhu
# @File    : numpy_reshape.py
# @task description :
import numpy as np

a = np.arange(6).reshape(2, 3)
aT = a.T
print(a)
print(np.shape(a))
print("*"*89)
print(aT)
print(np.shape(aT))

