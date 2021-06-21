# -*-coding:utf-8-*-
# @Time    : 2019/10/11 0011 14:43
# @Author  :zhu
# @File    : mytf_10.py
# @task description :
import tensorflow as tf
import numpy as np
import warnings
warnings.filterwarnings("ignore")


t1 = tf.constant([[1,  2], [3, 4], [5, 6]])
t2 = tf.constant([1,  2, 5, 6])
t3 = tf.constant([[1,  2], [3, 4], [5, 6]])
t4 = [[6], [7]]
t5 = [[6, 7, 9, 78, 23], [6, 7, 9, 78, 23]]
t6 = tf.ones((6,))
result_2 = tf.arg_max(t5)
# t3 = tf.multiply(t1, t2)
result_1 = t1 - t3
# result_2 = tf.multiply(t1, t2)
# result_3 = tf.reduce_sum(tf.reduce_sum(result_2, axis=1), axis=0)
# t5 = tf.zeros([96, 30])
init = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)
    print(result_2.eval())

#     print(np.shape(t_list))
#     print(np.shape(t_list1))
#     print(t_list1.eval())
#     # print()
#     # print()
#     # print(t7.eval())
#     # print()
#     # print(t8.eval())

