# -*-coding:utf-8-*-
# @Time    : 2019/5/16 0016 17:51
# @Author   :zhuxinquan
# @File    : mytf_03.py

import tensorflow as tf


state = tf.Variable(0, name='counter')



one = tf.constant(1)
print(one)
exit()

new_value = tf.add(state, one)

updata = tf.assign(state, new_value)


init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(0, 4):
        sess.run(updata)
        print(sess.run(state))


