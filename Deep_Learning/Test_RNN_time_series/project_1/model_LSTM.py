# -*-coding:utf-8-*-
# @Time    : 2019/10/29 0029 16:53
# @Author  :zhu
# @File    : model_LSTM.py
# @task description :
import tensorflow as tf
from tensorflow.contrib import layers as tflayers



def weight_variable(shape):  ###这里定义的是全连接的参数w
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):  ###这里定义的是全连接的参数b
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def lstm_cell3(model='lstm', rnn_size=[128, 128], keep_prob=0.8):  ###定义LSTM层
    if model == 'lstm':
        cell_func = tf.contrib.rnn.BasicLSTMCell
    elif model == 'gru':
        cell_func = tf.contrib.rnn.GRUCell
    elif model == 'rnn':
        cell_func = tf.contrib.rnn.BasicRNNCell
    cell = []
    for unit in rnn_size:  ###定义多层LSTM
        cell.append(tf.contrib.rnn.DropoutWrapper(cell_func(unit, state_is_tuple=True),
                                                  output_keep_prob=keep_prob))  ###使用的dropout
    return tf.contrib.rnn.MultiRNNCell(cell, state_is_tuple=True)


def dnn_stack(input, layers):  ###全连接层使用tflayers里面的stack，这样不用自己手动写连接
    if layers and isinstance(layers, dict):
        dnn_out = tflayers.stack(input, tflayers.fully_connected,
                                 layers['layers'],
                                 activation_fn=layers.get('activation')
                                 )
    elif layers:
        dnn_out = tflayers.stack(input, tflayers.fully_connected, layers)
    W_fc1 = weight_variable([layers['layers'][-1], 1])
    b_fc1 = bias_variable([1])
    pred = tf.add(tf.matmul(dnn_out, W_fc1), b_fc1, name='dnnout')  ###dnn的输出结果和label对应是一个数字
    return pred


def lstm_cell(model='lstm', rnn_size=128, num_layers=2, keep_prob=0.8):
    if model=='lstm':
        cell_func=tf.contrib.rnn.BasicLSTMCell
    elif model=='gru':
        cell_func=tf.contrib.rnn.GRUCell
    elif model=='rnn':
        cell_func=tf.contrib.rnn.BasicRNNCell
    cell=cell_func(rnn_size, state_is_tuple = True)
    return tf.contrib.rnn.MultiRNNCell(
        [tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=keep_prob)]*num_layers,
        state_is_tuple=True)



batch_size = 32

input_data = tf.placeholder("float", shape=[None, 5, 1])
input_label = tf.placeholder("float", shape=[None, 1])

# 定义LSTM
rnncell = lstm_cell()
initial_state = rnncell.zero_state(batch_size, tf.float32)
output, state = tf.nn.dynamic_rnn(rnncell, inputs=input_data, initial_state=initial_state, time_major=False)    # LSTM的结果

# LSTM结果输入dnn
dnn_out = dnn_stack(output[:, -1, :], layers={'layers': [32, 16]})
loss = tf.reduce_sum(tf.pow(dnn_out-input_label, 2))    # 平方和损失
learning_rate = tf.Variable(0.0, trainable=False)
tvars = tf.trainable_variables()
grads, _ = tf.clip_by_global_norm(tf.gradients(loss, tvars), 5)     # 计算梯度
optimizer = tf.train.AdamOptimizer(learning_rate)
train_op = optimizer.apply_gradients(zip(grads, tvars))

"""生成数据"""
from Test_RNN_time_series.project_1.rnn_makeData import generator, rnn_data_format, DataSet
x = generator(1000)
X = rnn_data_format(x, 5)

y = rnn_data_format(x, 5, label=True)

trainds = DataSet(X, y)



epoch = 30
batch = len(X) // batch_size


print("training.....")
saver = tf.train.Saver(tf.global_variables())
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epo in range(epoch):
        sess.run(tf.assign(learning_rate, 0.002 * (0.97 ** epo)))
        all_loss = 0.0
        for bat in range(batch):
            x_, y_ = trainds.next_batch(batch_size=batch_size)
            train_loss, _ = sess.run([loss, train_op], feed_dict={input_data: x_, input_label: y_})
            all_loss = all_loss + train_loss
        print(epoch, ' Loss: ', all_loss * 1.0 / batch)
    saver.save(sess, './rnn/lstm_time_series.model')

