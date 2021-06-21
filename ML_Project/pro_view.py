# -*-coding:utf-8-*-
# @Time    : 2019/9/27 0027 13:57
# @Author  :zhu
# @File    : pro_view.py
# @task description :


import tensorflow as tf
import numpy as np
import Example_matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (14, 8)
# 生成随机数
n_observations = 100
xs = np.linspace(-3, 3, n_observations)
ys = np.sin(xs) + np.random.uniform(-0.5, 0.5, n_observations)
plt.scatter(xs, ys)
plt.show()
# 定义容器,放入X和Y
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")
# 定义权重和偏置,对应与一次线性函数y = wx + b
w = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")
# 进行计算预测Y_Pre
Y_Pre = tf.add(tf.multiply(X, w), b)
# 计算损失的函数值,就是平方差
loss = tf.square(Y - Y_Pre, name="loss")
# 初始化
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
# 给出迭代次数,并且加入 Session执行
n_samples = xs.shape[0]
init = tf.global_variables_initializer()
with tf.Session() as sess:
    # 首先初始化所有的变量
    sess.run(init)
    # 写入日记,使用tensorboard观察
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    result_loss = []
    # 训练模型
    for i in range(50):
        total_loss = 0
        for x, y in zip(xs, ys):
            # 通过feed_dic把数据灌进去
            _, l = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
            total_loss += l
        if i % 5 == 0:
            print('Epoch {0}: {1}'.format(i, total_loss / n_samples))



    # 关闭writer
    writer.close()
    w, b = sess.run([w, b])

print(w, b)
print("W:" + str(w[0]))
print("b:" + str(b[0]))

plt.plot(xs, ys, "bo", label="Real data")
plt.plot(xs, xs * w + b, 'r', label="Predicted data")
plt.legend()
plt.show()