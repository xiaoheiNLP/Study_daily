# -*-coding:utf-8-*-
# @Time    : 2019/10/21 0021 15:30
# @Author  :zhu
# @File    : mytf_16.py
# @task description
import tensorflow as tf




vector = tf.Variable([7., 7.], 'vector')
# Make vector norm as small as possible.
loss = tf.reduce_sum(tf.square(vector))
# Ensure the vector's y component is = 1.
equalities = [vector[1] - 1.]
# Ensure the vector's x component is >= 1.
inequalities = [vector[0] - 1.]
# Our default SciPy optimization algorithm, L-BFGS-B, does not support
# general constraints. Thus we use SLSQP instead.
optimizer = tf.contrib.opt.ScipyOptimizerInterface(
  loss, equalities=equalities, inequalities=inequalities, method='SLSQP')


with tf.Session() as session:
  optimizer.minimize(session)
# The value of vector should now be [1., 1.].
