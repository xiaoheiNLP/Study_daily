# -*-coding:utf-8-*-
# @Time    : 2019/10/14 0014 15:16
# @Author  :zhu
# @File    : myscipy_2.py
# @task description :
# coding=utf-8

import math
n = 200000
prime = [i for i in range(1, n+1)]
r = int(math.sqrt(n))
for j in range(2, r+1):
  s = j*j
  while s <= n:
    prime[s-1] = 0
    s = s+j
print(sum(prime)-1)
