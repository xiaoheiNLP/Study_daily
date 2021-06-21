# -*-coding:utf-8-*-
# @Time    : 2019/12/6 0006 17:30
# @Author  :zhu
# @File    : myNumpy_1.py
# @task description :
import numpy as np

def numpy_1():
    t1 = np.array([1, 2, 3])
    t2 = np.array([1, 2, 3])
    t3 = t1 + t2
    print(t3)
    t1 = [1, 2, 3]
    t2 = [1, 2, 3]
    t3 = t1 + t2
    print(t3)
    """
    n
    """


def test_zip():
    t1 = ["a", "b", "c"]
    t1_dict = dict(zip([i for i in range(len(t1))], t1))
    print(t1_dict)


if __name__ == '__main__':
    # numpy_1()
    test_zip()

