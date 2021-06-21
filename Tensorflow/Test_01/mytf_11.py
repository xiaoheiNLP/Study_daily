# -*-coding:utf-8-*-
# @Time    : 2019/10/11 0011 10:03
# @Author  :zhu
# @File    : mytf_09.py
# @task description :
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")
import numpy as np


t = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

t3 = tf.constant(np.random.random(96), dtype=tf.float32)

t4 = tf.constant(np.random.random(96), dtype=tf.float32)
t4_1 = tf.transpose(tf.expand_dims(t4, 0))

# t5 = tf.matmul(t3, t4_1)
init = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)
    print(t3.eval())
    print()
    print(t4.eval())
    print()
    print(t4_1.eval())

