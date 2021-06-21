#3 -*-coding:utf-8-*-
# @Time    : 2019/11/26 0026 17:04
# @Author  :zhu
# @File    : tensorBoard_2.py
# @task description :
"""
tensorBoard可视化的实例：

# 运行命令是:tensorboard --logdir=C:\Users\Administrator\Desktop\MyProject\Study_daily\Test_tensorflow\TensorBoard\tensorBoard_2 --host=127.0.0.1
参考学习地址：https://blog.csdn.net/gg_18826075157/article/details/78447253
"""

import os
import tensorflow as tf
from tensorflow.contrib import slim     # tf的一个轻量级库
from tensorflow.examples.tutorials.mnist import input_data
import time
t1 = time.time()

def cnn_model(learning_rate):
    with tf.Graph().as_default() as graph:
        mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
        x = tf.placeholder(tf.float32, shape=[None, 784])
        y = tf.placeholder(tf.float32, shape=[None, 10])
        x_train = tf.reshape(x, [-1, 28, 28, 1])
        tf.summary.image('input', x_train, 10)

        with slim.arg_scope([slim.conv2d, slim.fully_connected],
                normalizer_fn=slim.batch_norm,
                activation_fn=tf.nn.relu):
            with slim.arg_scope([slim.max_pool2d], padding='SAME'):
                conv1 = slim.conv2d(x_train, 32, [5, 5])
                conv_vars = tf.get_collection(tf.GraphKeys.MODEL_VARIABLES, 'Conv')
                tf.summary.histogram('conv_weights', conv_vars[0])
                pool1 = slim.max_pool2d(conv1, [2, 2])
                conv2 = slim.conv2d(pool1, 64, [5, 5])
                pool2 = slim.max_pool2d(conv2, [2, 2])
                flatten = slim.flatten(pool2)
                fc = slim.fully_connected(flatten, 1024)

        logits = slim.fully_connected(fc, 10, activation_fn=None)
        softmax = tf.nn.softmax(logits, name='output')

        with tf.name_scope('loss'):
            loss = slim.losses.softmax_cross_entropy(logits, y)
            tf.summary.scalar('loss', loss)

        train_op = slim.optimize_loss(loss, slim.get_or_create_global_step(),
                learning_rate=learning_rate,
                optimizer='Adam')

        with tf.name_scope('accuracy'):
            correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            tf.summary.scalar('accuracy', accuracy)
        summary = tf.summary.merge_all()

    return {'x': x, 'y': y, 'accuracy': accuracy, 'summary': summary, 'mnist': mnist}, train_op, graph


for learning_rate in [0.1, 0.01, 0.001]:
    vars, train_op, graph = cnn_model(learning_rate)
    with tf.Session(graph=graph) as sess:
        log_dir = os.path.join('tensorBoard_2', 'cnn-lr-{}'.format(learning_rate))
        print("log_dir:", log_dir)
        writer = tf.summary.FileWriter(log_dir, sess.graph)
        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        for i in range(500):
            batch = vars['mnist'].train.next_batch(50)
            if i % 100 == 0:
                train_accuracy = vars['accuracy'].eval(feed_dict={vars['x']: batch[0],
                    vars['y']: batch[1]})
                print("step %d, training accuracy %g"%(i, train_accuracy))
            _, w_summary = sess.run([train_op, vars['summary']],
                    feed_dict={vars['x']: batch[0], vars['y']: batch[1]})
            writer.add_summary(w_summary, i)
print("消耗时间是：", time.time()-t1)

