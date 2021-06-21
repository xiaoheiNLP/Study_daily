# -*-coding:utf-8-*-
# @Time    : 2019/10/25 0025 16:19
# @Author  :zhu
# @File    : rnn_makeData.py
# @task description :
# 参考学习地址：https://blog.csdn.net/zhxchstc/article/details/79261617
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.contrib import layers as tflayers
import pysnooper

def generator(x):
    return [np.sin(i * 0.06) for i in range(x)]

# @pysnooper.snoop()
def rnn_data_format(data, timestep=7, label=False):
    data = pd.DataFrame(data)
    rnn_data = []
    if label:  # label是二维数组，[样本数，1]
        for i in range(len(data) - timestep):
            rnn_data.append([x for x in data.iloc[i + timestep].as_matrix()])
    else:  # 样本是3维数组[样本数，time_step，1]
        for i in range(len(data) - timestep):
            rnn_data.append([x for x in data.iloc[i:(i + timestep)].as_matrix()])
    return np.array(rnn_data, dtype=np.float32)


class DataSet(object):
    def __init__(self, x, y):
        self._data_size = len(x)
        self._epochs_completed = 0
        self._index_in_epoch = 0
        self._data_index = np.arange(len(x))
        self.x = x
        self.y = y

    def next_batch(self, batch_size):
        start = self._index_in_epoch
        if start + batch_size >= self._data_size:
            np.random.shuffle(self._data_index)
            self._index_in_epoch = 0
            start = self._index_in_epoch
            end = self._index_in_epoch + batch_size
            self._index_in_epoch = end
        else:
            end = self._index_in_epoch + batch_size
            self._index_in_epoch = end
        batch_x, batch_y = self.get_data(start, end)
        return np.array(batch_x, dtype=np.float32), np.array(batch_y, dtype=np.float32)

    def get_data(self, start, end):
        batch_x = []
        batch_y = []
        for i in range(start, end):
            batch_x.append(self.x[self._data_index[i]])
            batch_y.append(self.y[self._data_index[i]])
        return batch_x, batch_y



x = generator(10)
X = rnn_data_format(x, 5)

y = rnn_data_format(x, 5, label=True)

trainds = DataSet(X, y)



"""
生成数据就显得很复杂
"""




