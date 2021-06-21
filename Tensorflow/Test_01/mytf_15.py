# -*-coding:utf-8-*-
# @Time    : 2019/10/11 0011 14:43
# @Author  :zhu
# @File    : mytf_10.py
# @task description :
import tensorflow as tf
import numpy as np
import warnings
warnings.filterwarnings("ignore")

x = tf.constant([-1, -2, 5, 6], dtype=tf.float32)
x_result = tf.tanh(x)

init = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)
    # print(a.eval())
    print(x.eval())
    print(x_result.eval())

