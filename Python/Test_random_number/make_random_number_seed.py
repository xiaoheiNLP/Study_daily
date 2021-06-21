# -*- coding: utf-8 -*-
# @Time    : 2019-07-03 23:37
# @Author  : xinquan
# @File    : make_random_number_seed.py


def test():
    import numpy as np
    SEED = 234550  # 产生统一的随机数

    # 基于seed产生随机数，这是根据随机种子产生随机数的一种常用方法，要熟练运用
    rdm = np.random.RandomState(SEED)
    # 随机数返回32行2列的矩阵 表示32组 体积和重量 作为输入数据集。因为这里没用真实的数据集，所以这样操作。
    X = rdm.rand(32, 2)
    print(X)


if __name__ == '__main__':
    test()

