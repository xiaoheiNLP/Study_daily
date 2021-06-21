# -*-coding:utf-8-*-
# @Time    : 2019/10/12 0012 15:41
# @Author  :zhu
# @File    : mytf_12.py
# @task description :

import warnings
import numpy as np
import tensorflow as tf
warnings.filterwarnings("ignore")


def print_loss(loss_evaled, vector_evaled):
  print(loss_evaled, vector_evaled)

vector = tf.Variable([7., 7.], 'vector')
loss = tf.reduce_sum(tf.square(vector))

optimizer = tf.contrib.opt.ScipyOptimizerInterface(
    loss, method='L-BFGS-B',
    options={'maxiter': 100},
    var_to_bounds={vector: ([-5, 2], np.infty)}
)

with tf.Session() as session:
  tf.global_variables_initializer().run()
  optimizer.minimize(session,
                     loss_callback=print_loss,
                     fetches=[loss, vector],
                     feed_dict={})
  print("打印结果")
  print(vector.eval())


"""
partial move to tensorflow/addons
部分移动到tensorflow/addons
98.0 [7. 7.]
79.28232 [6.2317786 6.3598156]
5.0 [1. 2.]
打印结果
[1. 2.]
"""