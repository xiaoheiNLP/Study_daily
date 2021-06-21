# -*-coding:utf-8-*-
# @Time    : 2019/5/16 0016 18:03
# @Author   :zhuxinquan
# @File    : mytf_04.py

import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.add(input1, input2)


with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1:[2.0],
                                      input2:[8.0]
                                      }))

