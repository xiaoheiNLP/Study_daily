# -*-coding:utf-8-*-
# @Time    : 2019/5/16 0016 17:29
# @Author   :zhuxinquan
# @File    : mytf_02.py

import tensorflow as tf
import numpy as np
import time

value = np.random.randn(5000, 1000)
a = tf.constant(value)

b = a * a

c = 0
tic = time.time()
with tf.Session() as sess:
    for i in range(1000):
        sess.run(b)

        c += 1
        if c % 100 == 0:
            d = c / 10
            # print(d)
            print("计算进行%s%%" % d)
