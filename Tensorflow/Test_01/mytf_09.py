# -*-coding:utf-8-*-
# @Time    : 2019/10/11 0011 10:03
# @Author  :zhu
# @File    : mytf_09.py
# @task description :
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")
import numpy as np
#
# a = np.array([[-1, 2], [2, 3]])
# b = np.array([[3, 4], [4, 5]])
# print('\n a:\n', a)
# print('\n b:\n', b)
# # a + b，矩阵相加
# print("\n a+b: \n", a+b)

t3 = tf.constant([0], dtype=tf.float32)
t4 = tf.expand_dims(t3, 1)
init = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init)
    print(t3.eval())
    print(t4.eval())

