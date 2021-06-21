# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 23:07
# @Author  : xinquan
# @File    : RNN_04.py
"""


学习地址:
    https://www.cnblogs.com/wanyu416/p/9009985.html

"""


# 生成一个简单的反向传播算法
def test():
    import tensorflow as tf
    import numpy as np

    BATCH_SIZE = 8  # 一次输入网络的数据，称为batch。一次不能喂太多数据
    SEED = 234550  # 产生统一的随机数

    # 基于seed产生随机数，这是根据随机种子产生随机数的一种常用方法，要熟练运用
    rdm = np.random.RandomState(SEED)
    # 随机数返回32行2列的矩阵 表示32组 体积和重量 作为输入数据集。因为这里没用真实的数据集，所以这样操作。
    X = rdm.rand(32, 2)
    # 从X这个32行2列的矩阵中 取出一行 判断如果和小于1 给Y赋值1 如果和不小于1 给Y赋值0 （这里只是人为的定义），作为输入数据集的标签（正确答案）
    Y_ = [[int(x0 + x1 < 1)] for (x0, x1) in X]
    print("X:\n", X)
    print("Y_:\n", Y_)

    # 1定义神经网络的输入、参数和输出,定义前向传播过程。
    x = tf.placeholder(tf.float32, shape=(None, 2))
    y_ = tf.placeholder(tf.float32, shape=(None, 1))

    w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
    w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

    a = tf.matmul(x, w1)
    y = tf.matmul(a, w2)

    # 2定义损失函数及反向传播方法。
    loss = tf.reduce_mean(tf.square(y - y_))    # 计算张量tensor沿着指定的数轴（tensor的某一维度）上的的平均值，主要用作降维或者计算tensor（图像）的平均值
    train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)  # 三种优化方法选择一个就可以
    # train_step = tf.train.MomentumOptimizer(0.001,0.9).minimize(loss_mse)
    # train_step = tf.train.AdamOptimizer(0.001).minimize(loss_mse)

    # 3生成会话，训练STEPS轮
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        # 输出目前（未经训练）的参数取值。
        print("w1:\n", sess.run(w1))
        print("w2:\n", sess.run(w2))
        print("\n")

        # 训练模型。
        STEPS = 3000
        for i in range(STEPS):  # 0-2999
            start = (
                                i * BATCH_SIZE) % 32  # i=0,start=0,end=8;i=1,start=8,end=16;i=2,start=16,end=24;i=3,start=24,end=32;i=4,start=0,end=8。也就是说每次训练8组数据，一共训练3000次。
            end = start + BATCH_SIZE
            sess.run(train_step, feed_dict={x: X[start:end], y_: Y_[start:end]})
            if i % 500 == 0:
                total_loss = sess.run(loss, feed_dict={x: X, y_: Y_})
                print("After %d training step(s), loss on all data is %g" % (i, total_loss))

        # 输出训练后的参数取值。
        print("\n")
        print("w1:\n", sess.run(w1))
        print("w2:\n", sess.run(w2))


if __name__ == '__main__':
    test()      # 反向传播的实现

