# -*-coding:utf-8-*-
# @Time    : 2019/11/25 0025 17:31
# @Author  :zhu
# @File    : du_test.py
# @task description :
import numpy as np

def get_x_y(data, N, offset):
    """
    Split data into x (features) and y (target)
    """
    x, y = [], []
    for i in range(offset, len(data)):
        # print(i)
        x.append(data[i - N:i])
        y.append(data[i])
    x = np.array(x)
    y = np.array(y)

    return x, y


if __name__ == '__main__':
    my_data = [t for t in range(10)]
    # print(data)
    # exit()
    t_x, t_y = get_x_y(data=my_data, N=2, offset=3)
    print(t_x)
    print(t_y)

