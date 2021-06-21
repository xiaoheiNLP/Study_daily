# -*-coding:utf-8-*-
# @Time    : 2019/5/16 0016 18:12
# @Author   :zhuxinquan
# @File    : mytf_05.py


import warnings
warnings.filterwarnings("ignore")
from scipy import optimize


# oop =optimize.minimize(constraints=)

import tensorflow as tf

import tensorflow as tf
vector = tf.Variable([7., 7.], 'vector')
# Make vector norm as small as possible.
loss = tf.reduce_sum(tf.square(vector))


optimizer = tf.contrib.opt.ScipyOptimizerInterface(
    loss, options={'maxiter': 100})     # method="SLSQP"

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    print(session.run(vector))  # results: [7.0, 7.0]
    optimizer.minimize(session)
    print(session.run(vector))  # results: [ -1.88996808e-06  -1.88996808e-06]
