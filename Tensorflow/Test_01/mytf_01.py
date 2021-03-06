# -*-coding:utf-8-*-
# @Time    : 2019/5/15 0015 10:00
# @Author   :zhuxinquan
# @File    : mytf_01.py
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
import numpy as np

x_data = np.float32(np.random.rand(2, 200))
y_data = np.dot([0.100, 0.200], x_data) + 0.300
# print(x_data)
# print(y_data)
# print(np.shape(x_data), np.shape(y_data))
# exit()

# 构建一个线性模型
b = tf.Variable(tf.zeros(1))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))        # 误差
optimizer = tf.train.GradientDescentOptimizer(0.5)      # 优化器:减小误差
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()        #

# 启动图 (graph)
sess = tf.Session()
sess.run(init)      # 激活


# with tf.Session as sess:
# 拟合平面
for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))




