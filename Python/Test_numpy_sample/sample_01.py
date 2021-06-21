# -*-coding:utf-8-*-
# @Time    : 2019/6/11 0011 16:40
# @Author   :zhuxinquan
# @File    : sample_01.py


import multiprocessing
import time


def func(x):
    return x*x


if __name__ == "__main__":
    # pool = multiprocessing.Pool(processes=4)  # 创建4个进程
    # results = []
    # for i in range(10):
    #
    #     results.append(pool.apply_async(func, (i,)))
    # pool.close()  # 关闭进程池，表示不能再往进程池中添加进程，需要在join之前调用
    # pool.join()  # 等待进程池中的所有进程执行完毕
    # print("Sub-process(es) done.")
    #
    # for i in results:
    #     print(i.get())
    t = [12, 12, 54, 76, 7]
    print(max(t))
    print(min(t))

    import numpy as np
    print(np.max(np.array([1, 4, 65, 1, 2])))

