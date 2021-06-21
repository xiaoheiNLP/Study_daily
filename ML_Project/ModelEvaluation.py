# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 1:58 下午
# @Author  : xinquan
# @File    : ModelEvaluation.py
"""
模型评估的


"""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# 准确率:准确率是分类正确的样本占总样本个数的比例
def func1():
    y_pred = [0, 2, 1, 3]
    y_true = [0, 2, 2, 3]
    print(accuracy_score(y_true, y_pred))  # 0.5
    print(accuracy_score(y_true, y_pred, normalize=False))  # 2


# 精确率:精确率指 模型预测为正的样本中 实际也为正的样本 占 被预测为正的样本的比例
# 精确率最好的值是1，最差的值是0.
def func2():
    """
    参数
    y_true : 一维数组，或标签指示符 / 稀疏矩阵，实际（正确的）标签.
    y_pred : 一维数组，或标签指示符 / 稀疏矩阵，分类器返回的预测标签.
    labels : 列表，可选值. 当average != binary时被包含的标签集合，如果average是None的话还包含它们的顺序. 在数据中存在的标签可以被排除，比如计算一个忽略多数负类的多类平均值时，数据中没有出现的标签会导致宏平均值（marco average）含有0个组件. 对于多标签的目标，标签是列索引. 默认情况下，y_true和y_pred中的所有标签按照排序后的顺序使用.
    pos_label : 字符串或整型，默认为1. 如果average = binary并且数据是二进制时需要被报告的类. 若果数据是多类的或者多标签的，这将被忽略；设置labels=[pos_label]和average != binary就只会报告设置的特定标签的分数.
    average : 字符串，可选值为[None, ‘binary’ (默认), ‘micro’, ‘macro’, ‘samples’, ‘weighted’]. 多类或 者多标签目标需要这个参数. 如果为None，每个类别的分数将会返回. 否则，它决定了数据的平均值类型.
    ‘binary’: 仅报告由pos_label指定的类的结果. 这仅适用于目标（y_{true, pred}）是二进制的情况.
    ‘micro’: 通过计算总的真正性、假负性和假正性来全局计算指标.
    ‘macro’: 为每个标签计算指标，找到它们未加权的均值. 它不考虑标签数量不平衡的情况.
    ‘weighted’: 为每个标签计算指标，并通过各类占比找到它们的加权均值（每个标签的正例数）.它解决了’macro’的标签不平衡问题；它可以产生不在精确率和召回率之间的F-score.
    ‘samples’: 为每个实例计算指标，找到它们的均值（只在多标签分类的时候有意义，并且和函数accuracy_score不同）.
    sample_weight : 形状为[样本数量]的数组，可选参数. 样本权重.
     
    ————————————————
    版权声明：本文为CSDN博主「hfutdog」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/hfutdog/article/details/88085878
    :return:
    """
    y_true = [0, 1, 2, 0, 1, 2]
    y_pred = [0, 2, 1, 0, 0, 1]
    print(precision_score(y_true, y_pred, average='macro'))  # 0.2222222222222222
    print(precision_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    print(precision_score(y_true, y_pred, average='weighted'))  # 0.2222222222222222
    print(precision_score(y_true, y_pred, average=None))  # [0.66666667 0.         0.        ]


# 召回率:召回率指实际为正的样本中被预测为正的样本所占实际为正的样本的比例
def func3():
    y_true = [0, 1, 2, 0, 1, 2]
    y_pred = [0, 2, 1, 0, 0, 1]
    print(recall_score(y_true, y_pred, average='macro'))  # 0.3333333333333333
    print(recall_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    print(recall_score(y_true, y_pred, average='weighted'))  # 0.3333333333333333
    print(recall_score(y_true, y_pred, average=None))  # [1. 0. 0.]


# F1:F1 score是精确率和召回率的调和平均值
def func4():
    y_true = [0, 1, 2, 0, 1, 2]
    y_pred = [0, 2, 1, 0, 0, 1]
    print(f1_score(y_true, y_pred, average='macro'))  # 0.26666666666666666
    print(f1_score(y_true, y_pred, average='micro'))  # 0.3333333333333333
    print(f1_score(y_true, y_pred, average='weighted'))  # 0.26666666666666666
    print(f1_score(y_true, y_pred, average=None))  # [0.8 0.  0. ]


if __name__ == '__main__':
    func4()

"""
参考地址：https://blog.csdn.net/hfutdog/article/details/88085878
"""
