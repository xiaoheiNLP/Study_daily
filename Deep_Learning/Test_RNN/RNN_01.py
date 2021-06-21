# -*-coding:utf-8-*-
# @Time    : 2019/7/3 0003 14:19
# @Author   :zhuxinquan
# @File    : RNN_01.py
"""
实践几个简单的RNN
学习的地址
https://mp.weixin.qq.com/s?__biz=MzIzNDM2OTMzOQ==&mid=2247485800&idx=1&sn=4d03fc1d6c3e2bda2a000762c24b6603&chksm=e8f6313cdf81b82a644b10f8101f1162b370eada67d7f005e503ee8f855de5c965adb7c50e26&scene=21#wechat_redirect
"""

import tensorflow as tf

"""
拥有5个循环神经元的一层RNN网络，其中激活函数用tanh,并且假设该RNN仅运行两个时刻，每个时刻的输入向量的大小为3，通过两个时刻来显示
"""
def test01():
    n_inputs = 3    # 初始化数据的维度
    n_neurons = 5   # 神经元的个数
    X0 = tf.placeholder(tf.float32, [None, n_inputs])
    X1 = tf.placeholder(tf.float32, [None, n_inputs])
    Wx = tf.Variable(tf.random_normal(shape=[n_inputs, n_neurons], dtype=tf.float32))
    Wy = tf.Variable(tf.random_normal(shape=[n_neurons, n_neurons], dtype=tf.float32))
    b = tf.Variable(tf.zeros([1, n_neurons], dtype=tf.float32))

    Y0 = tf.tanh(tf.matmul(X0, Wx) + b)
    Y1 = tf.tanh(tf.matmul(Y0, Wy) + tf.matmul(X1, Wx) + b)
    init = tf.global_variables_initializer()

    # 在两个时刻都对模型进行输入数据
    import numpy as np
    # Mini-batch: instance 0,instance 1,instance 2,instance 3
    X0_batch = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 0, 1]])   # t = 0
    X1_batch = np.array([[9, 8, 7], [0, 0, 0], [6, 5, 4], [3, 2, 1]])   # t = 1
    with tf.Session() as sess:
        init.run()
        Y0_val, Y1_val = sess.run([Y0, Y1], feed_dict={X0: X0_batch, X1: X1_batch})

    print(Y0_val)


def test02():
    n_inputs = 3
    n_neurons = 5
    X0 = tf.placeholder(tf.float32, [None, n_inputs])
    X1 = tf.placeholder(tf.float32, [None, n_inputs])
    basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)   # 可以把这个函数想象为一个创建记忆单元的一个工厂，用来构建展开的RNN网络
    output_seqs, states = tf.contrib.rnn.static_rnn(
        basic_cell, [X0, X1], dtype=tf.float32
    )
    Y0, Y1 = output_seqs
    print(Y0)

def test02_2():
    import numpy as np
    n_inputs = 3
    n_neurons = 5
    X = tf.placeholder(tf.float32, [None, 2, n_inputs])   # 其中第一维度None代表mini-batch的大小，第二个维度代表时间步长的个数，也就是有多少个时刻。第三个维度为每个时刻的输入大小
    X_seqs = tf.unstack(tf.transpose(X, perm=[1, 0, 2]))
    basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)
    output_seqs, states = tf.contrib.rnn.static_rnn(    # 调用静态RNN
        basic_cell, X_seqs, dtype=tf.float32)

    # outputs, states = tf.nn.dynamic_rnn(basic_cell, X, dtype=tf.float32)
    # 调用动态RNN，似乎需要GPU版本的tf

    outputs = tf.transpose(tf.stack(output_seqs), perm=[1, 0, 2])
    init = tf.global_variables_initializer()
    X_batch = np.array([
        # t = 0 t = 1
        [[0, 1, 2], [9, 8, 7]],  # instance 0
        [[3, 4, 5], [0, 0, 0]],  # instance 1
        [[6, 7, 8], [6, 5, 4]],  # instance 2
        [[9, 0, 1], [3, 2, 1]],  # instance 3
    ])
    with tf.Session() as sess:
        init.run()
        outputs_val = outputs.eval(feed_dict={X: X_batch})
    print(outputs_val)


if __name__ == '__main__':
    # test01()    # RNN的简单实现
    test02_2()    # 静态RNN的实现

