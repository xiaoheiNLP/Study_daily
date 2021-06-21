# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 3:44 下午
# @Author  : xinquan
# @File    : StudyNumpy.py

import numpy as np

def test111():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.ndim)
    print(np.shape(a))

def test222():
    a = np.array([2, 3, 4, 5])
    b = np.array([8, 5, 4])
    c = np.array([5, 4, 6, 8, 3])
    ax, bx, cx = np.ix_(a, b, c)
    print(cx)

def test333():
    a = np.array([2, 3, 4, 5])
    b = np.array([8, 5, 4])
    c = np.array([5, 4, 6, 8, 3])
    ax, bx, cx = np.ix_(a, b, c)

    print(ax.shape, bx.shape, cx.shape)

    result = ax + bx * cx
    print(result)
    print(np.shape(result))
    print(result[3])
    print(result[3, 2])
    print(result[3, 2, 4])
    # 17
    print("*"*89)
    print(a[3])
    print(b[2])
    print(c[4])

    # a[3] + b[2] * c[4]


def test4():
    arr = np.arange(10)
    print(arr)
    out = np.where(arr % 2 == 1, -2, arr)
    print(out)
    print(arr)
    arr[arr % 2 == 1] = -1
    print(arr)

if __name__ == '__main__':
    # test111()
    test4()
