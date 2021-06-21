# -*-coding:utf-8-*-
# @Time    : 2019/8/29 0029 15:19
# @Author  :zhu
# @File    : pro_svm.py.py
# @task description : 用tf简单实现一下svm
import warnings
warnings.filterwarnings('ignore')

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
import Example_matplotlib.pyplot as plt
import numpy as np

t_x = np.linspace(-1, 1, 50, dtype=np.float32)

noise = np.random.normal(0, 0.05, t_x.shape)
t_y = t_x * 3.0 + 5.0 + noise


x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
a = tf.Variable(0.0)
b = tf.Variable(0.0)
curr_y = x * a + b
epsilon = tf.constant([0.20])

# 训练
learning_rate = 0.001
training_epochs = 1000


# 损失函数: subtract张量的减法
loss = tf.reduce_sum(tf.maximum(0., tf.subtract(tf.abs(tf.subtract(curr_y, y)), epsilon)))
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(training_epochs):
    sess.run(train, {x: t_x, y: t_y})
    if i % 20 == 0:
        print(i, sess.run([a, b, loss], {x: t_x, y: t_y}))

a_val = sess.run(a)
b_val = sess.run(b)
print("this model is y=", a_val, "* x +", b_val)
# sess.close()

y_learned = t_x * a_val + b_val

plt.plot(t_x, t_y, "k.")
plt.plot(t_x, y_learned, "g-")
linewidth = sess.run(epsilon)
plt.plot(t_x, y_learned+linewidth, "r--")
plt.plot(t_x, y_learned-linewidth, "r--")
plt.savefig("svm.png")
plt.show()







